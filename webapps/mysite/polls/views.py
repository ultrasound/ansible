from django.shortcuts import get_object_or_404, render

from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = { # This is matched Django template tag in template's file
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #try:
    question = get_object_or_404(Question, pk=question_id)
    #except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
    #return  HttpResponse("you are looking at question %s." % question_id)
    return render(request, 'pools/detail.html', {'question': question})

def results(request, question_id):
    response = "Your are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# for mentor
import json
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

def questions(request, question_id):
    question_detail = serializers.serialize('json', Question.objects.all())
    output = [d['fields'] for d in json.loads(question_detail)]
    return JsonResponse({'question': output})

    """
    if request.method == 'GET':
        return render(request, )
    elif request.method == 'POST':
        do_somethind_else()
        return HttpResponse(json)
    """