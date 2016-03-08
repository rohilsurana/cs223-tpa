from django.contrib import admin
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from . import models

# Register your models here.

admin.site.register([models.Faculty, models.Student])
admin.site.site_header = ugettext_lazy('Objective Exam Management')
admin.site.site_title = ugettext_lazy('Objective Exam Management')