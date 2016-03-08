from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^out/', views.logout_page, name='out'),
    url(r'', views.dashboard),
]