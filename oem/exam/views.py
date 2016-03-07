from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from .models import Test

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