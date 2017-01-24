from django.forms import ModelForm
from .models import Post


class postform(ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'article_title', 'article_content']