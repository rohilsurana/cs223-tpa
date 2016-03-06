from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')