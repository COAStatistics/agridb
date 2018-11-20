from django.contrib import admin
from .models import (
    Profile,
    Livestock,
    InvestigationType,
    Investigation,
    Field,
    CountType,
)

# Register your models here.
admin.site.register(Livestock)
admin.site.register(InvestigationType)
admin.site.register(Investigation)
admin.site.register(Field)
admin.site.register(CountType)
admin.site.register(Profile)