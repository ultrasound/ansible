from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # the 'name' values as called by the {% url %} template tag
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='result'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # for mentor
    url(r'^question/([0-9]+)/$', views.questions, name='questions'),
]