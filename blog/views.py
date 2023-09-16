from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.views import generic, View
from .models import Post, Category, Comment
from .forms import PostForm, EditProfileForm, CommentForm
from django.contrib.auth.forms import PasswordChangeForm
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

        editors_pick = get_object_or_404(Post, slug="ais-impact-on-todays-programmers")

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


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


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
            comment_count = Comment.objects.filter(post=post, approved=True).count()
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
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
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

        for post in posts:
            comment_count = Comment.objects.filter(post=post, approved=True).count()
            posts_with_comment_count.append((post, comment_count))

        return render(
            request,
            "profile.html",
            {
                "user": user,
                "posts_with_comment_count": posts_with_comment_count,
                "favourites": favourites,
            },
        )


class AddPost(generic.CreateView):
    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateProfileView(View):
    template_name = "update_profile.html"
    user_form_class = EditProfileForm
    password_form_class = PasswordChangeForm

    def get_context_data(self, user_form=None, password_form=None):
        user = self.request.user
        context = {
            "user_form": user_form or self.user_form_class(instance=user),
            "password_form": password_form or self.password_form_class(user),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user

        user_form = self.user_form_class(request.POST, instance=user)
        password_form = self.password_form_class(user, request.POST)

        if "password_change" in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(self.request, self.request.user)
                return redirect("profile")
            else:
                context = self.get_context_data(password_form=password_form)
                return render(request, self.template_name, context)

        if "update_profile" in request.POST:
            if user_form.is_valid():
                user_form.save()
                return redirect("profile")
            else:
                context = self.get_context_data(user_form=user_form)
                print(context)
                return render(request, self.template_name, context)

        if "delete_account" in request.POST:
            self.object = self.get_object()
            self.object.delete()
            return redirect("home")

        context = self.get_context_data(
            user_form=user_form, password_form=password_form
        )
        return render(request, self.template_name, context)
