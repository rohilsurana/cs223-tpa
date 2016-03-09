from django.contrib import admin
# from nested_inline.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
import nested_admin
from django.utils.translation import ugettext_lazy
from django.forms import forms
from . import models


# Register your models here.

# class ChoiceInlineFormSet(nested_admin.N):
#     pass

class ChoiceInlineFormset(nested_admin.formsets.NestedInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            try:
                if form.cleaned_data.get('is_correct'):
                    count += 1
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        if count!=1:
            raise forms.ValidationError('Only one choice can be correct.')
        pass


class ChoiceInline(nested_admin.NestedTabularInline):
    formset = ChoiceInlineFormset
    model = models.Choice
    extra = 1


class QuestionInline(nested_admin.NestedTabularInline):
    model = models.Question
    inlines = [ChoiceInline]
    extra = 1


class TestAdmin(nested_admin.NestedModelAdmin):

    def get_queryset(self, request):
        qs = super(TestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(course__faculty__exact=request.user)


    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(TestAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'course':
            if request.user is not None:
                field.queryset = field.queryset.filter(faculty__exact=request.user)
            else:
                field.queryset = field.queryset.none()

        return field
    list_display = ('__str__', 'start_time', 'end_time')
    model = models.Test
    inlines = [QuestionInline]


admin.site.register(models.Test, TestAdmin)
admin.site.register([models.Course, models.TestResult])
admin.site.site_header = ugettext_lazy('Objective Exam Management')
admin.site.site_title = ugettext_lazy('Objective Exam Management')
