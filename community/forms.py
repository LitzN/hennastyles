from django import forms
from .models import Post, Comment, Like


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('heading', 'body', 'image', 'user_profile')

    image = forms.ImageField(
            label='Image', required=False)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
        self.field[field].label = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'user_profile', 'for_post')

    body = forms.CharField(
        label=None, required=True
    )


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('post', 'user')