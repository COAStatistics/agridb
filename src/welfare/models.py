from django.db.models import (
    Model,
    CASCADE,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKey,
)

# Create your models here.


class ElderlyAllowance(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.member


class FarmerInsurance(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.member


class Scholarship(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member')
    name = CharField(max_length=50, null=True, verbose_name='Name')
    subsidy = IntegerField(verbose_name='subsidy')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{} {} {}".format(self.member, self.name, self.subsidy)
