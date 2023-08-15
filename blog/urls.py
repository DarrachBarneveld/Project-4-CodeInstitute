from . import views
from django.urls import path


urlpatterns = [
    path("", views.CategoryList.as_view(), name="home"),
    path("<slug:slug>/", views.CategoryPostsView.as_view(), name="category_posts"),
    path("post/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
