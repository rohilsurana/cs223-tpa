from django import forms
from django.contrib import admin
from django.forms.widgets import RadioSelect
from django.forms.models import BaseInlineFormSet
from django.utils.translation import ugettext_lazy


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one service has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one item required.')


class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(TestForm, self).__init__(*args, **kwargs)
        if questions:
            self.title = questions[0].test.course.name + " - " + questions[0].test.name

        index = 1
        for question in questions:
            choice_fields = [(choice.id, str(choice)) for choice in question.choice_set.all()]

            self.fields['question_text-' + str(question.pk)] = forms.CharField(initial=question.question_text, label="Q-" + str(index), disabled=True)
            self.fields['question_text-' + str(question.pk)].widget.attrs['readonly'] = True
            self.fields['question_text-' + str(question.pk)].widget.attrs.update({'style':'font-size:20; border:none; background-color: white; color:black;'})

            self.fields['question-' + str(question.pk)] = forms.ChoiceField(choices=choice_fields, widget=RadioSelect, label='', required=False)
            index += 1
