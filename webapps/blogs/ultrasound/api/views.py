from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def post_list(request):
    data = [
        {'id':1, 'title': 'title 1'},
    ]
    return JsonResponse(data, safe=False)