from . import views
from django.urls import path


urlpatterns = [
    path("", views.CategoryList.as_view(), name="home"),
    path("add_post", views.AddPost.as_view(), name="add_post"),
    path("profile", views.Profile.as_view(), name="profile"),
    path("<slug:slug>/", views.CategoryPosts.as_view(), name="category_posts"),
    path("post/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
