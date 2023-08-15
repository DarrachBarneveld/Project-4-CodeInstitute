from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Category


# Create your views here.
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "index.html"


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


class CategoryPostsView(View):
    template_name = "category_posts.html"

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, title=slug)
        category_list = Category.objects.all()
        posts = Post.objects.filter(category=category)

        return render(
            request,
            "category_posts.html",
            {
                "posts": posts,
                "category_list": category_list,
            },
        )
