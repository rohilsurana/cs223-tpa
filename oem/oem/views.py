from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from exam.models import Test, Course
from authentication.models import Student, User


def main_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('log:in') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('admin:index'))
    if not hasattr(request.user, 'Student'):
        return HttpResponseRedirect(reverse('log:out'))
    student_data = request.user.Student.courses.test_set.filter("start_date")
    return render(request, 'base.html') # This is just a sample page add a new template for this