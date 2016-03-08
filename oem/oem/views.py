from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from exam.models import Test, Course
from authentication.models import Student, User


def main_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('log:in') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return faculty_view(request)
    elif not hasattr(request.user, 'student'):
        return HttpResponseRedirect(reverse('log:out'))
    else:
        student_view(request)


def faculty_view(request):
    faculty_courses = request.user.courses_set.all()

    faculty_students = Student.objects.filter(courses__in=faculty_courses).order_by('username')

    return render(request, 'base.html')

def student_view(request):

    student_courses = request.user.student.courses.all()

    student_tests = Test.objects.filter(course__in=student_courses).order_by('start_time').all()

    students_results = request.user.testresult_set.all()

    return render(request, 'base.html') # This is just a sample page add a new template for this