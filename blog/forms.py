from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["excerpt"].widget = forms.Textarea(attrs={"rows": 3})

    class Meta:
        model = Post
        fields = ["title", "category", "excerpt", "content", "featured_image"]
        widgets = {"content": SummernoteWidget()}


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        help_texts = {"username": None}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
