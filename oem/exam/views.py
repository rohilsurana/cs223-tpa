from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Test, TestResult, Choice
from django.core.urlresolvers import reverse
from .forms import TestForm


# View to generate the test form for students
def give_test(request, test_id):
    test_data = Test.objects.get(pk=test_id)
    question_list = test_data.question_set.all()
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('log:in') + '?next=' + request.get_full_path())
    if not test_data.authenticate_student_user(request.user):
        return HttpResponseRedirect('/')  # render a page with written you are unathorized to take this test

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST, questions=question_list)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return submit_test(request, test_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm(questions=question_list)

    return render(request, 'test.html', {'form': form})


def submit_test(request, test_id):
    question_list = Test.objects.get(pk=test_id).question_set.all()
    correct_count = 0
    marks = 0

    for question in question_list:  # looping over all questions
        # now match if user has selected correct choice
        question_string = 'question-' + str(question.pk)
        if not question_string in request.POST:
            continue
        if Choice.objects.get(pk=int(request.POST[question_string])).is_correct:
            marks += question.marks
            correct_count += 1
            # end of checking answers

    # Save it to database
    result = TestResult(test=Test.objects.get(pk=test_id), student=request.user, marks=marks)
    result.save()

    return render_to_response("test_submit.html", {"correct_count": correct_count, "marks": marks})
