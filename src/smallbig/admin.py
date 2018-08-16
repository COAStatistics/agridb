from django.contrib import admin
from . import models

admin.site.register(models.LandlordRetire)
admin.site.register(models.LandlordRent)
admin.site.register(models.TenantTransfer)
admin.site.register(models.Tenant)
