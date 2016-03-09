from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from exam.models import Test, Course, TestResult
from authentication.models import Student, User


def main_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return faculty_view(request)
    elif not hasattr(request.user, 'student'):
        return HttpResponseRedirect(reverse('logout'))
    else:
        return student_view(request)


def faculty_view(request):
    faculty_name = request.user.name
    faculty_courses = request.user.course_set.all()

    #faculty_students = Student.objects.filter(courses__in=faculty_courses).order_by('username')

    return render(request, 'faculty_view.html', {'faculty_name' : faculty_name, 'faculty_courses' : faculty_courses})


def faculty_course_view(request, course_id):
    course = Course.objects.get(pk=course_id)

    student_list = course.student_set.all()         # list of all student attending that course
    mark_list = [[]]                                  # 2d array of student's marks, ith row of this array stores marks obtained by ith student in all the tests

    index = 0
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    for student in student_list:
        mark_list.append([])
        for test in test_list:
            try:
                mark = TestResult.objects.get(student=student, test=test).marks
            except:
                mark = None
            mark_list[index].append(mark)
        index += 1
    return render(request, 'faculty_view.html', {'course_name' : course.name, 'student_list' : student_list, 'marks' : mark_list, 'tests' : test_list})


def student_view(request):

    student_name = request.user.student.name
    student_courses = request.user.student.courses.all()

    student_tests = Test.objects.filter(course__in=student_courses).order_by('start_time').all()
    students_results = []

    for test in student_tests:
        try:
            mark = TestResult.objects.get(student=request.user, test=test).marks
        except:
            mark = None
        students_results.append(mark)

    #students_results = request.user.testresult_set.all()

    return render(request, 'student_view.html', {'student_name' : student_name, 'student_courses' : student_courses,
                                                 'student_result' : students_results})


def course_graph_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    test_average = []

    for test in test_list:

        test_results = TestResult.objects.filter(test=test).all()
        test_marks = []
        for result in test_results:
            test_marks.append(result.marks)

        average = 0
        for marks in test_marks:
            average += marks
        if len(test_marks) > 0:
            average /= len(test_marks)
        test_average.append(average)

    graph_data = []
    for test_name, average in zip(test_list, test_average):
        graph_data.append([test_name, average])

    return render(request, 'lineChart.html', {'course_name' : course.name, 'data' : graph_data})


def student_course_graph_view(request, course_id, student_id):

    student = Student.obejects.get(pk=student_id)
    course = Course.objects.get(pk=course_id)
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    test_result = []

    for test in test_list:
        try:
            marks = TestResult.objects.get(student=student, test=test).marks
        except:
            marks = None

        test_result.append(marks)

    graph_data = []
    for test_name, result in zip(test_list, test_result):
        graph_data.append([test_name, result])

    return render(request, 'lineChart.html', {'course_name' : course.name, 'data' : graph_data})
