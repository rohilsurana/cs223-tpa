from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Problem Statement', {'fields': ['question_text']}),
        ('Marks', {'fields': ['marks']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','marks')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)