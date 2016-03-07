from django import forms
from django.forms.widgets import RadioSelect

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('question')
        super(TestForm, self).__init(*args, **kwargs)
        counter = 1
        for question in questions:
            choice_fields = [x for x in question.choice_set.all()]
            self.fields['question-' + str(counter)] = forms.ChoiceField(choices=choice_fields, widget=RadioSelect)
            counter += 1