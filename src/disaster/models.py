from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    DateTimeField,
    DateField,
    FloatField,
)

# Create your models here.


class DisasterEvent(Model):
    name = CharField(max_length=50, verbose_name='Name', unique=True)
    date = DateField(auto_now=False, auto_now_add=False, null=False, default='1911-01-01')
    update_time = DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "Name:{}, Date:{}".format(self.name, self.date)


class Disaster(Model):
    member = ForeignKey('household.member', on_delete=CASCADE, verbose_name='Member', related_name='disasters')
    event = ForeignKey('disaster.DisasterEvent', on_delete=CASCADE, verbose_name='Event', related_name='disasters')
    crop = ForeignKey('fallow.crop', on_delete=CASCADE, verbose_name='Crop', related_name='disasters')
    area = FloatField(verbose_name='Area')
    subsidy = PositiveIntegerField(verbose_name='Subsidy')
    update_time = DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}, {} ".format(self.member, self.event, self.crop)
