from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import update_session_auth_hash
from django.views import generic, View
from .models import Post, Category, Comment
from .forms import (
    PostForm,
    EditProfileForm,
    CommentForm,
    EditBioForm,
    CustomPasswordChangeForm,
)
from django.contrib.auth.models import User
from django.db.models import Count


# Create your views here.
class CategoryList(View):
    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.filter(approved=True)
        popular_post = (
            all_posts.annotate(comment_count=Count("comments"))
            .order_by("-comment_count")
            .first()
        )

        popular_post.comment_count = Comment.objects.filter(
            post=popular_post, approved=True
        ).count()

        trending_posts = all_posts.annotate(like_count=Count("likes")).order_by(
            "-like_count"
        )[:3]

        editors_pick = get_object_or_404(
            Post, slug="ais-influence-on-tech-shaping-the-future"
        )

        editors_pick.comment_count = Comment.objects.filter(
            post=editors_pick, approved=True
        ).count()

        return render(
            request,
            "home.html",
            {
                "all_posts": all_posts,
                "popular_post": popular_post,
                "trending_posts": trending_posts,
                "editors_pick": editors_pick,
            },
        )


class CategoryPosts(generic.ListView):
    template_name = "index.html"
    paginate_by = 6

    def get(self, request, slug, *args, **kwargs):
        if slug == "All":
            posts = Post.objects.all()

        else:
            category = get_object_or_404(Category, title=slug)
            posts = Post.objects.filter(category=category)

        # Create a Paginator object
        paginator = Paginator(posts, self.paginate_by)

        for post in posts:
            post.comment_count = Comment.objects.filter(
                post=post, approved=True
            ).count()

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get("page")

        # Get the Page object for the current page
        page = paginator.get_page(page_number)

        return render(
            request,
            "index.html",
            {"posts": page, "category": slug},
        )


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        newslug = slug.split("/")[-1]
        post = get_object_or_404(queryset, slug=newslug)
        popular_posts = Post.objects.filter(
            category=post.category, approved=True
        ).exclude(pk=post.id)
        popular_posts_with_comment_count = []

        for pop_post in popular_posts:
            comment_count = Comment.objects.filter(post=pop_post, approved=True).count()
            popular_posts_with_comment_count.append((pop_post, comment_count))

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "popular_posts": popular_posts_with_comment_count,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        newslug = slug.split("/")[-1]
        post = get_object_or_404(queryset, slug=newslug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            print(request.user)
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class Profile(View):
    def get(self, request, slug, *args, **kwargs):
        # user = request.user
        queryset = User.objects.filter(username=slug)
        user = get_object_or_404(queryset)
        posts = Post.objects.filter(approved=True, author=user)
        posts_with_comment_count = []
        favourites = user.blogpost_like.all()
        total_posts = posts.__len__
        total_comments = 0
        total_likes = 0

        print(user.id)

        for post in posts:
            total_likes += post.number_of_likes()
            comment_count = Comment.objects.filter(post=post, approved=True).count()
            total_comments += comment_count
            posts_with_comment_count.append((post, comment_count))

        return render(
            request,
            "profile.html",
            {
                "profile": user,
                "total_posts": total_posts,
                "total_comments": total_comments,
                "total_likes": total_likes,
                "posts_with_comment_count": posts_with_comment_count,
                "favourites": favourites,
            },
        )


class AddPost(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    # success_url = reverse_lazy("home")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            return HttpResponseForbidden("You don't have permission to edit this post.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", args=[self.object.slug])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object  # Pass the post instance to the form
        return kwargs


class UpdateProfileView(View):
    template_name = "update_profile.html"
    user_form_class = EditProfileForm
    password_form_class = CustomPasswordChangeForm
    bio_form_class = EditBioForm

    def get_context_data(self, user_form=None, password_form=None, bio_form=None):
        user = self.request.user
        context = {
            "user_form": user_form or self.user_form_class(instance=user),
            "password_form": password_form or self.password_form_class(user),
            "bio_form": bio_form or self.bio_form_class(instance=user.profile),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user

        user_form = self.user_form_class(request.POST, instance=user)
        password_form = self.password_form_class(user, request.POST)
        bio_form = self.bio_form_class(request.POST, instance=user.profile)

        if "bio_change" in request.POST:
            if bio_form.is_valid():
                bio_form.save()
                context = self.get_context_data(bio_form=bio_form)
                return render(request, self.template_name, context)

            else:
                context = self.get_context_data(user_form=bio_form)
                return render(request, self.template_name, context)

        if "password_change" in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(self.request, self.request.user)
                context = self.get_context_data(password_form=password_form)
                return render(request, self.template_name, context)
            else:
                context = self.get_context_data(password_form=password_form)
                return render(request, self.template_name, context)

        if "update_profile" in request.POST:
            if user_form.is_valid():
                user_form.save()
                context = self.get_context_data(user_form=user_form)
                return render(request, self.template_name, context)

            else:
                print("valid")
                context = self.get_context_data(user_form=user_form)
                return render(request, self.template_name, context)

        if "delete_account" in request.POST:
            self.object = self.get_object()
            self.object.delete()
            return redirect("home")

        context = self.get_context_data(
            user_form=user_form, password_form=password_form, bio_form=bio_form
        )
        return render(request, self.template_name, context)
