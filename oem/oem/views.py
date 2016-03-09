from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User as auth_user
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
    faculty_name = request.user.username
    faculty_courses = request.user.course_set.all()

    #faculty_students = Student.objects.filter(courses__in=faculty_courses).order_by('username')

    return render(request, 'faculty_view.html', {'faculty_courses' : faculty_courses})


def faculty_course_view(request, course_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
    elif hasattr(request.user, 'student'):
        return HttpResponseRedirect(reverse('logout'))

    course = get_object_or_404(Course, pk=course_id)

    student_list = course.student_set.values_list('user',flat=True)         # list of all student attending that course
    mark_list = []                                  # 2d array of student's marks, ith row of this array stores marks obtained by ith student in all the tests
    student_list = auth_user.objects.filter(pk__in=student_list).all()
    index = 0
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    for student in student_list:
        marks = []
        for test in test_list:
            try:
                mark = TestResult.objects.get(student=student, test=test).marks
            except:
                mark = None
            marks.append((test, mark))
        mark_list.append((student, marks))
        index += 1

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
        graph_data.append((test_name.name, average))

    return render(request, 'faculty_course_view.html', {'course_name' : course.name, 'student_list' : student_list,
                                                        'marks' : mark_list, 'tests': test_list, 'data' : graph_data})


def student_view(request):

    student_name = request.user.student.name
    student_courses = request.user.student.courses.all()

    student_tests = Test.objects.filter(course__in=student_courses).order_by('start_time').all()
    students_test_results = []

    for test in student_tests:
        try:
            mark = TestResult.objects.get(student=request.user, test=test).marks
        except:
            mark = None
        students_test_results.append((test, mark))

    #students_results = request.user.testresult_set.all()

    return render(request, 'student_view.html', {'student_courses' : student_courses,
                                                 'student_test_result' : students_test_results})


# def course_graph_view(request, course_id):
#
#     if not request.user.is_authenticated():
#         return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
#     if request.user.is_staff:
#         if request.user.is_superuser:
#             return HttpResponseRedirect(reverse('admin:index'))
#     elif hasattr(request.user, 'student'):
#         return HttpResponseRedirect(reverse('logout'))
#
#     course = Course.objects.get(pk=course_id)
#     test_list = Test.objects.filter(course=course).order_by('start_time').all()
#     test_average = []
#
#     for test in test_list:
#
#         test_results = TestResult.objects.filter(test=test).all()
#         test_marks = []
#         for result in test_results:
#             test_marks.append(result.marks)
#
#         average = 0
#         for marks in test_marks:
#             average += marks
#         if len(test_marks) > 0:
#             average /= len(test_marks)
#         test_average.append(average)
#
#     graph_data = []
#     for test_name, average in zip(test_list, test_average):
#         graph_data.append([test_name, average])
#
#     return render(request, 'lineChart.html', {'course_name' : course.name, 'data' : graph_data})


def student_course_graph_view(request, course_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
    if not hasattr(request.user, 'student') and not request.user.is_staff:
        return HttpResponseRedirect(reverse('logout'))

    student = request.user
    course = get_object_or_404(Course, pk=course_id)
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    test_result = []
    print(test_list)
    for test in test_list:
        try:
            marks = TestResult.objects.get(student=student, test=test).marks
        except:
            marks = 0

        test_result.append(marks)

    graph_data = []
    for test, result in zip(test_list, test_result):
        graph_data.append((str(test.name), result))

    return render(request, 'lineChart.html', {'course_name' : course.name, 'data' : graph_data})


def student_faculty_course_graph_view(request, student_id, course_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
    if not hasattr(request.user, 'student') and not request.user.is_staff:
        return HttpResponseRedirect(reverse('logout'))

    student = get_object_or_404(auth_user, pk=student_id)
    course = get_object_or_404(Course, pk=course_id)
    test_list = Test.objects.filter(course=course).order_by('start_time').all()
    test_result = []
    print(test_list)
    for test in test_list:
        try:
            marks = TestResult.objects.get(student=student, test=test).marks
        except:
            marks = 0

        test_result.append(marks)

    graph_data = []
    for test, result in zip(test_list, test_result):
        graph_data.append((str(test.name), result))

    return render(request, 'lineChart.html', {'course_name' : course.name, 'data' : graph_data})


def faculty_test_view(request,test_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
    if request.user.is_staff:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
    elif hasattr(request.user, 'student'):
        return HttpResponseRedirect(reverse('logout'))

    test = get_object_or_404(Test,pk=test_id)

    if test.course.faculty != request.user:
        return HttpResponseRedirect(reverse('admin:index'))
    students = test.course.student_set.values_list('user',flat=True)
    students = auth_user.objects.filter(pk__in=students).all()
    marks = []
    for student in students:
        try:
            print(student)
            print(test)
            mark = TestResult.objects.get(student=student, test=test).marks
        except Exception as e:
            print(e)
            mark = None
        marks.append((student,mark))
    return render(request, 'faculty_test_view.html',{'test': test, 'marks': marks})