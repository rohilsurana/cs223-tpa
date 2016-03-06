from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^', login),
    url(r'^out/', views.logout_page),
]