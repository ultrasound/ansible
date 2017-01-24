from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

# Create your views here.

def post_list(request):
    post_list = []
    for post in Post.objects.all():
        post_list.append({
            'id':post.id,
            'title':post.title,
            'content':post.content,
        })
    return JsonResponse(post_list, safe=False)
