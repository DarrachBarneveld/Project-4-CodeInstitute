"""Views"""

# pylint: disable=E1101


from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.response import TemplateResponse
from django.contrib.auth import update_session_auth_hash
from django.views import generic, View
from .models import Post, Category, Comment, Profile
from .forms import (
    PostForm,
    EditProfileForm,
    CommentForm,
    EditBioForm,
    CustomPasswordChangeForm,
)


# Create your views here.
class CategoryList(View):
    """
    A view class for displaying a list of categories and featured posts on the homepage.

    """

    def get(self, request, *args, **kwargs):
        """
        Retrieves the posts from the database and returns the most popular, trending by likes
        and editors pick

        """
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

        print(request.user)

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
    """
    A view class for displaying a list of posts based on a specific category.

    """

    template_name = "index.html"
    paginate_by = 6

    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves the posts related to a category from the database
        """
        if slug == "All":
            posts = Post.objects.all()

        else:
            category = get_object_or_404(Category, title=slug)
            posts = Post.objects.filter(category=category, approved=True)

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
    """
    A view class for displaying and managing individual post details.

    Methods:
    - `get`: Handles GET requests to display post details, comments, and related posts.
    - `post`: Handles POST requests for commenting on or deleting comments on a post.

    """

    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves the post, comments and popular related posts from the database
        """
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
        """
        This method is called when a POST request is made to the view
        via the comment form or delete comment.
        """
        queryset = Post.objects.filter(approved=True)
        newslug = slug.split("/")[-1]
        post = get_object_or_404(queryset, slug=newslug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if "delete_comment" in request.POST:
            comment_id = request.POST.get("comment_id")
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return redirect("/")

        if comment_form.is_valid():
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
    """
    Handles the liking/unliking of a post.

    Methods:
    - post: Handles the POST request to like or unlike a post and redirects the
      user to the post's detail page.
    """

    def post(self, request, slug):
        """
        Handles the liking/unliking of a post and redirects to the post's detail page.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class ProfileView(View):
    """
    Displays the user profile page with user information and their posts.

    Methods:
    - get: Handles the GET request to display the user profile page.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Handles the GET request to display the user profile page.

        Args:
        - request: The HTTP request object.
        - slug: The slug of the user's profile.

        Returns:
        - HttpResponse: Renders the user profile page with user information
          and statistics.
        """
        profile = get_object_or_404(Profile, slug=slug)
        user = get_object_or_404(User, username=profile)

        posts = Post.objects.filter(author=user, approved=True)
        pending_posts = Post.objects.filter(author=user, approved=False)
        posts_with_comment_count = []
        favourites = user.blogpost_like.all().filter(approved=True)
        total_posts = posts.__len__
        total_comments = 0
        total_likes = 0

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
                "pending_posts": pending_posts,
                "total_posts": total_posts,
                "total_comments": total_comments,
                "total_likes": total_likes,
                "posts_with_comment_count": posts_with_comment_count,
                "favourites": favourites,
            },
        )


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    Allows a logged-in user to create a new blog post.

    Methods:
    - form_valid: Overrides the base method to set the post author to the
      currently logged-in user before saving the form.

    Mixins:
    - LoginRequiredMixin: Ensures that only authenticated users can access
      this view.
    """

    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, generic.UpdateView):
    """
    Allows a logged-in user to edit an existing blog post.

    - get_queryset: Filters the queryset to only include posts authored by
      the currently logged-in user.
    - dispatch: Overrides the base method to handle the case where the post
      is not found and returns a custom template response.
    - post: Handles HTTP POST requests, allowing the user to delete their post.
    - form_valid: Overrides the base method to set the post as unapproved after
      editing.
    - get_form_kwargs: Overrides the base method to provide the instance to the
      form.

    Mixins:
    - LoginRequiredMixin: Ensures that only authenticated users can access
      this view, and they must be the author of the post.
    """

    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    success_url = "/"

    def get_queryset(self):
        """
        Filters the queryset to include only posts authored by the user.

        Returns:
        - QuerySet: A filtered queryset containing the user's authored posts.
        """
        return Post.objects.filter(author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        """
        Handles the view's dispatch, including handling non-existent posts.

        Returns:
        - TemplateResponse: Renders a custom template for non-existent posts.
        """
        try:
            self.get_object()
        except Http404:
            return TemplateResponse(self.request, "no_permission.html")

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handles HTTP POST requests, allowing the user to delete their post.

        Returns:
        - HttpResponseRedirect: Redirects to the success URL after post deletion.
        """
        if "delete_post" in request.POST:
            post = self.get_object()
            post.delete()
            return redirect("/")

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Handles a valid form submission and sets the post as unapproved.

        Returns:
        - HttpResponse: Redirects to the success URL after saving the post.
        """
        form.instance.approved = False
        return super().form_valid(form)

    def get_form_kwargs(self):
        """
        Provides the instance to the form.

        Returns:
        - dict: A dictionary containing keyword arguments for the form.
        """

        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


class UpdateProfileView(View):
    """
    Allows a user to update their profile information, including username,
    password, and bio.

    Methods:
    - get_context_data: Retrieves context data for rendering the profile update
      page, including user information and forms.
    - get: Handles HTTP GET requests for rendering the profile update page.
    - post: Handles HTTP POST requests for processing form submissions and
      updating the profile information.
    """

    template_name = "update_profile.html"
    user_form_class = EditProfileForm
    password_form_class = CustomPasswordChangeForm
    bio_form_class = EditBioForm

    def get_context_data(self, user_form=None, password_form=None, bio_form=None):
        """
        Retrieves context data for rendering the profile update page.
        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """
        user = self.request.user
        context = {
            "user_form": user_form or self.user_form_class(instance=user),
            "password_form": password_form or self.password_form_class(user),
            "bio_form": bio_form or self.bio_form_class(instance=user.profile),
        }
        return context

    def get(self, request, *args, **kwargs):
        """
        Handles HTTP GET requests for rendering the profile update page.

        Returns:
        - HttpResponse: Renders the profile update page with context data.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handles HTTP POST requests for processing form submissions and updating
        profile information.

        Returns:
        - HttpResponse: Renders the profile update page with context data after
          processing the form submissions.
        """

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
            user.delete()
            return redirect("home")

        context = self.get_context_data(
            user_form=user_form, password_form=password_form, bio_form=bio_form
        )
        return render(request, self.template_name, context)
