from django.contrib import admin
from django.utils.translation import ugettext_lazy
from . import models

# Register your models here.


admin.site.register([models.Faculty, models.Student])
admin.site.site_header = ugettext_lazy('Objective Exam Management')
admin.site.site_title = ugettext_lazy('Objective Exam Management')