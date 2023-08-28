from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm


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

    template_name = "update_profile.html"
    user_form_class = EditProfileForm
    password_form_class = PasswordChangeForm

    def get_context_data(self):
        user = self.request.user
        context = {
            "user_form": self.user_form_class(instance=user),
            "password_form": self.password_form_class(user),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = self.user_form_class(request.POST, instance=user)
        password_form = self.password_form_class(user, request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "User information updated.")
            return redirect("profile")

        if password_form.is_valid():
            new_password = password_form.cleaned_data["new_password1"]
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password changed successfully.")
            return redirect("profile")

        context = {
            "user_form": user_form,
            "password_form": password_form,
        }
        return render(request, self.template_name, context)


class Profile(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        posts = Post.objects.filter(approved=True, author=user)

        return render(request, "profile.html", {"user": user, "posts": posts})


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
            "user_form": self.user_form_class(instance=user),
            "password_form": self.password_form_class(user),
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
            print("fire")
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
