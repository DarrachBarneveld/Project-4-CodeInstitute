from . import views
from django.urls import path


urlpatterns = [
    path("", views.CategoryList.as_view(), name="home"),
    path("'<slug:slug>/'", views.CategoryPostsView.as_view(), name="category_posts"),
]
