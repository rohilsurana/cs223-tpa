from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Test, TestResult
from .forms import TestForm


# Create your views here.

# View to generate the test form for students
def give_test(request, test_id):
    test_data = Test.objects.get(pk=test_id)
    question_list = test_data.question_set.all()
    if not request.user.is_authenticated():
        pass        # redirect to login page with next=test/pk
    if not test_data.authenticate_student_user(request.user):
        pass        # render a page with written you are unathorized to take this test

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST, questions=question_list)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm(questions=question_list)

    return render(request, 'test.html', {'form': form})


def submit_test(request, test_id):
    test_data = Test.objects.get(pk=test_id)
    question_list = test_data.question_set.all()
    correct_count = 0
    marks = 0

    for question in question_list:  # looping over all questions
        choices = question.choice_set.all()

        correct_index = 0
        for choice in choices:  # looping over all choices
            if choice.is_correct:
                break
            else:
                correct_index += 1

        # now match if user has selected correct choice
        if correct_index == request.POST['choice']:
            marks += question.marks
            correct_count += 1
            # end of matching

    # save it to database
    result = TestResult(test=test_id, student=request.user, marks=marks)
    result.save()

    return render_to_response("test_submit.html", {"correct_count": correct_count, "marks": marks})
