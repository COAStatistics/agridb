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
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member', related_name='elderly_allowances')
    year = ForeignKey('household.Year', on_delete=CASCADE, verbose_name='Year', related_name='elderly_allowances')
    subsidy = IntegerField(verbose_name='subsidy')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.member, self.year, self.subsidy)


class FarmerInsurance(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member', related_name='farmer_insurances')
    year = ForeignKey('household.Year', on_delete=CASCADE, verbose_name='Year', related_name='farmer_insurances')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}".format(self.member, self.year)


class Scholarship(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member', related_name='scholarships')
    year = ForeignKey('household.Year', on_delete=CASCADE, verbose_name='Year', related_name='scholarships')
    name = CharField(max_length=50, null=True, verbose_name='Name')
    subsidy = IntegerField(verbose_name='subsidy')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{} {} {}".format(self.member, self.name, self.subsidy)
