from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    return render_to_response("test_submit.html", {"correct_count": 1, "marks": 100})