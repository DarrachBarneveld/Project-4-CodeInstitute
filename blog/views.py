from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm, EditUserForm


# Create your views here.
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


class CategoryPosts(generic.ListView):
    template_name = "category_posts.html"
    paginate_by = 2

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, title=slug)
        category_list = Category.objects.all()
        posts = Post.objects.filter(category=category)

        # Create a Paginator object
        paginator = Paginator(posts, self.paginate_by)

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get("page")

        # Get the Page object for the current page
        page = paginator.get_page(page_number)

        return render(
            request,
            "category_posts.html",
            {
                "posts": page,
                "category_list": category_list,
            },
        )


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        newslug = slug.split("/")[-1]
        post = get_object_or_404(queryset, slug=newslug)

        return render(
            request,
            "post_detail.html",
            {"post": post},
        )


class Profile(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        posts = Post.objects.filter(approved=True, author=user)

        return render(request, "profile.html", {"user": user, "posts": posts})


class EditUserView(LoginRequiredMixin, UpdateView):
    template_name = "edit_user.html"
    success_url = reverse_lazy("profile")
    form_class = EditUserForm
    password_form_class = PasswordChangeForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_form"] = self.password_form_class(user=self.request.user)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        password_form = self.password_form_class(self.request.user, self.request.POST)
        print(password_form.is_valid())

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(self.request, self.request.user)

        return response

    def post(self, request, *args, **kwargs):
        password_form = self.password_form_class(self.request.user, self.request.POST)

        if password_form.is_valid() and "password_change" in request.POST:
            password_form.save()
            update_session_auth_hash(self.request, self.request.user)
            return redirect("home")
        if "delete_account" in request.POST:
            self.object = self.get_object()
            self.object.delete()
            return redirect("home")

        else:
            return super().post(request, *args, **kwargs)


class AddPost(generic.CreateView):
    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
