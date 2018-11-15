from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Household)
admin.site.register(models.Role)
admin.site.register(models.Member)
admin.site.register(models.Year)
