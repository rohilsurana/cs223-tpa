from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^(?P<test_id>[0-9]+)/$', views.give_test, name='test'),
]