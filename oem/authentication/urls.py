from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^in/', login, name='in'),
    url(r'^out/', views.logout_page, name='out'),
    url(r'', views.dashboard)
]