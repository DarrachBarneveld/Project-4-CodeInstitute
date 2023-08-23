from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Category
from .forms import PostForm


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
        post = get_object_or_404(queryset, slug="testing-post")
        print(slug)

        return render(
            request,
            "post_detail.html",
            {"post": post},
        )


class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     category_list = Category.objects.all()
    #     return render(
    #         request,
    #         "add_post.html",
    #         {"category_list": category_list, "post_form": PostForm()},
    #     )
