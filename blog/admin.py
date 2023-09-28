"""Admin page"""

from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment, Profile


class PostInline(admin.TabularInline):
    """
    Inline representation of blog posts for the admin panel.

    """

    model = Post
    fields = ("title", "approved", "excerpt")
    extra = 0


class ProfileInline(admin.StackedInline):
    """
    Inline representation of user profiles for the admin panel.

    """

    model = Profile


class UserAdmin(admin.ModelAdmin):
    """
    Admin model configuration for user accounts.

    This class defines the admin panel configuration for user accounts, allowing
    administrators to manage user information such as username, first name, last name,
    and email. It also includes an inline representation of user profiles using the
    `ProfileInline` class

    Example:
        To use this admin configuration for user accounts:

        admin.site.register(User, UserAdmin)

    """

    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin model configuration for post categories.

    """

    list_display = ("title",)
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin model configuration for posts.

    """

    list_display = ("title", "slug", "created_on", "approved")
    search_fields = ["title", "content"]
    list_filter = ("created_on", "category")
    actions = ["approve_posts"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

    def approve_posts(self, request, queryset):
        """
        Approve selected posts.

        This method is a custom action that allows administrators to approve selected
        posts by updating their "approved" field to True.
        """
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin model configuration for comments.

    """

    list_display = ("name", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        """
        Approve selected comments.

        This method is a custom action that allows administrators to approve selected
        comments by updating their "approved" field to True.
        """
        queryset.update(approved=True)
