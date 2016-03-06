from django.contrib import admin
# from nested_inline.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
import nested_admin
from django.utils.translation import ugettext_lazy
from . import models


# Register your models here.


class ChoiceInline(nested_admin.NestedTabularInline):
    model = models.Choice
    extra = 1


class QuestionInline(nested_admin.NestedStackedInline):
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

    model = models.Test
    inlines = [QuestionInline]


admin.site.register(models.Test, TestAdmin)
admin.site.register([models.Course])
admin.site.site_header = ugettext_lazy('Objective Exam Management')
admin.site.site_title = ugettext_lazy('Objective Exam Management')
