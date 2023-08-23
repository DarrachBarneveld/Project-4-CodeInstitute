from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


class PostInline(admin.TabularInline):
    model = Post
    fields = ("title", "approved", "excerpt")
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "approved")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on", "category")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
