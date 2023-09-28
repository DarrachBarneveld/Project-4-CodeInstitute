"""Forms"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserChangeForm
from django_summernote.widgets import SummernoteWidget

from .models import Post, Comment, Profile


class PostForm(forms.ModelForm):
    """
    A form for creating  blog post instances.

    """

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["excerpt"].widget = forms.Textarea(attrs={"rows": 3})

    class Meta:
        """Get post model, choose fields to display"""

        model = Post
        fields = ["title", "category", "excerpt", "content", "featured_image"]
        widgets = {"content": SummernoteWidget()}


class EditProfileForm(UserChangeForm):
    """
    A form for editing user profile information.

    """

    password = None

    def clean_username(self):
        """
        Clean and validate the username field.

        This method checks if the username contains spaces and raises a ValidationError
        if spaces are found.

        Returns:
            str: The cleaned and validated username.
        Raises:
            forms.ValidationError: If the username contains spaces.
        """
        username = self.cleaned_data.get("username")

        if " " in username:
            raise forms.ValidationError("Username cannot contain spaces.")

        return username

    class Meta:
        """Get User model, choose fields to display"""

        model = User
        fields = ["username", "email", "first_name", "last_name"]
        help_texts = {"username": None}


class EditBioForm(forms.ModelForm):
    """
    A form for editing user biography information.

    """

    class Meta:
        """Get Profile model, choose fields to display"""

        model = Profile
        fields = ["bio"]
        widgets = {
            "bio": forms.TextInput(),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    A customized form for changing a user's password.

    This form inherits from Django's built-in PasswordChangeForm and provides some custom
    modifications:

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove autofocus attribute from the old password field
        self.fields["old_password"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password1 field
        self.fields["new_password1"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password2 field
        self.fields["new_password2"].widget.attrs.pop("autofocus", None)


class CommentForm(forms.ModelForm):
    """
    A form for creating comments on blog posts.

    """

    class Meta:
        """Get Comment model, choose fields to display"""

        model = Comment
        fields = ("body",)
