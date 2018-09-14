from django.contrib import admin
from .models import (
    DisasterEvent,
    Disaster
)

# Register your models here.
admin.site.register(DisasterEvent)
admin.site.register(Disaster)