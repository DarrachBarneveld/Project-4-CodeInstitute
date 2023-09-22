from django.contrib import admin
from .models import Post, Category, Comment, Profile
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin


class PostInline(admin.TabularInline):
    model = Post
    fields = ("title", "approved", "excerpt")
    extra = 0


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline]


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ["bio"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "created_on", "approved")
    search_fields = ["title", "content"]
    list_filter = ("created_on", "category")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
