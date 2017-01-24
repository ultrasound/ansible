from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', views.post_list),
    url(r'^signup/$', 'views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),
    url(r'^$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/login/',
    }, name='logout_url'),
]