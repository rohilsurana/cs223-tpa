from django import forms
from django.forms.widgets import RadioSelect


class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(TestForm, self).__init__(*args, **kwargs)
        counter = 1
        for question in questions:
            choice_fields = [(choice.id, str(choice)) for choice in question.choice_set.all()]

            #self.fields['layout']
            self.fields['question_text-' + str(counter)] = forms.CharField(initial=question.question_text, label="")
            self.fields['question_text-' + str(counter)].disabled = True
            self.fields['question_text-' + str(counter)].widget.attrs.update({'style' : 'font-size:20; border:none; background-color: white; color:black;'})

            #self.fields['question_text-' + str(counter)]

            self.fields['question-' + str(counter)] = forms.ChoiceField(choices=choice_fields, widget=RadioSelect)
            self.fields['question-' + str(counter)].label = ''

            counter += 1