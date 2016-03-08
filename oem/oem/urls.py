"""oem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy
from django.conf import settings
from authentication.views import logout_page
from django.contrib.auth.views import login
from django.conf.urls.static import static
from .views import main_view

admin.site.site_header = ugettext_lazy('Obejctive Exam Management')
admin.site.site_title = ugettext_lazy('Obejctive Exam Management')

urlpatterns = [
    url(r'^$', main_view),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^logout/', logout_page, name='logout'),
    url(r'^login/', login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', include('exam.urls', namespace='exam')),
    url(r'dafuq', main_view)
] + static(settings.STATIC_URL)
