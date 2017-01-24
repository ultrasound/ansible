from django.forms import ModelForm
from .models import Post


class FeedbackFrom(ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'title', 'content']