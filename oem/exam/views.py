from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from .models import Test, TestResult

# Create your views here.
def give_test(request, test_id):
    test_data = Test.objects.get(pk = test_id)
    question_list = test_data.question_set.all()

    question_text = []          # question_text is a list containing all the text of questions of the TEST
    choice_array = [[]]         # choice array is 2d list, ith element of this contains all the choices of ith question

    i = 0
    for x in question_list:
        choice_array.append([])

        question_text.append(x.question_text)   # appended question text of ith question

        choices = x.choice_set.all()            # retrieved choice model of ith question

        for choice in choices:
            choice_array[i].append(choice.choice_text)
        i += 1

    choice_array.pop()

    return render_to_response("test.html", {"question_text" : question_text, "choice_array" : choice_array})


def submit_test(request, test_id):

    test_data = Test.objects.get(pk = test_id)
    question_list = test_data.question_set.all()
    correct_count = 0
    marks = 0

    for question in question_list:      # looping over all questions
        choices = question.choice_set.all()

        correct_index = 0
        for choice in choices:          # looping over all choices
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
    result = TestResult(test = test_id, student=request.user, marks=marks)
    result.save()

    return render_to_response("test_submit.html", {"correct_count" : correct_count, "marks" : marks})