from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["excerpt"].widget = forms.Textarea(attrs={"rows": 3})

    class Meta:
        model = Post
        fields = ["title", "category", "excerpt", "content", "featured_image"]
        widgets = {"content": SummernoteWidget()}
