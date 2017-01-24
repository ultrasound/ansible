from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

        return HttpResponseRedirect(
            reverse("signup_ok")
        )
    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "registration/signup.html", {
        "userform": userform,
    })