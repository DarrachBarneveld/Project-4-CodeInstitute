from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
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

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if " " in username:
            raise forms.ValidationError("Username cannot contain spaces.")

        return username

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        help_texts = {"username": None}


class EditBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio"]
        widgets = {
            "bio": forms.TextInput(),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove autofocus attribute from the old password field
        self.fields["old_password"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password1 field
        self.fields["new_password1"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password2 field
        self.fields["new_password2"].widget.attrs.pop("autofocus", None)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
