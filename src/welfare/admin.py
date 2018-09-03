from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.ElderlyAllowance)
admin.site.register(models.FarmerInsurance)
admin.site.register(models.Scholarship)