from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .form import postform

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            form.save()
        return None
    else:
        form = postform()

    return render(request, 'post.html', {'form': form})