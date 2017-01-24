from django.db import models

# Create your models here.

class Post(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    is_author = models.CharField(max_lenth=10)
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
