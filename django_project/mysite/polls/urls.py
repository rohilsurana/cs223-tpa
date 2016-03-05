from django.conf.urls import url
from . import views


# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# from django.views.generic.base import RedirectView

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.get_name, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#     url(r'^accounts/profile/$', RedirectView.as_view(url='/')), 
#     url(r'^accounts/$', RedirectView.as_view(url='/')),
]