from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    CASCADE,
    PositiveIntegerField,
    DateTimeField,
)

# Create your models here.


class DisasterEvent(Model):
    name = CharField(max_length=50, verbose_name='Name')
    update_time = DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Disaster(Model):
    member = ForeignKey('household.member', on_delete=CASCADE, verbose_name='Member')
    event = ForeignKey('disaster.DisasterEvent', on_delete=CASCADE, verbose_name='Event')
    crop = ForeignKey('fallow.crop', on_delete=CASCADE, verbose_name='Crop')
    area = PositiveIntegerField(verbose_name='Area')
    subsidy = PositiveIntegerField(verbose_name='Subsidy')
    update_time = DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}, {} ".format(self.member, self.event, self.crop)