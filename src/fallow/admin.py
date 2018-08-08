from django.contrib import admin
from . import models

admin.site.register(models.Crop)
admin.site.register(models.Declare)
admin.site.register(models.RiceArea)
admin.site.register(models.FallowTransfer)
admin.site.register(models.TransferCrop)
