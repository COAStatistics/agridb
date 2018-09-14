from django.db.models import (
    Model,
    CASCADE,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKey,
)

SEASON_CHOICES = [
    (1, 'Q1'),
    (2, 'Q2'),
    (3, 'Q3'),
    (4, 'Q4'),
]


class Livestock(Model):
    name = CharField(max_length=50, verbose_name='Name')
    parent = ForeignKey('self', blank=True, null=True, on_delete=CASCADE, verbose_name='Parent')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Investigation(Model):
    year = IntegerField(verbose_name='Year')
    season = CharField(max_length=1, choices=SEASON_CHOICES, verbose_name='Season')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return 'year:{0}, season:{1}'.format(self.year, self.season)


class CountType(Model):
    name = CharField(max_length=50, verbose_name='Name')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Field(Model):
    name = CharField(max_length=50, verbose_name='Name')
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Profile(Model):
    investigation = ForeignKey('livestock.Investigation', on_delete=CASCADE, verbose_name='Investigation')
    field = ForeignKey('livestock.Field', on_delete=CASCADE, verbose_name='Field')
    livestock = ForeignKey('livestock.Livestock', on_delete=CASCADE, verbose_name='Livestock')
    count_type = ForeignKey('livestock.CountType', on_delete=CASCADE, verbose_name='Count Type')
    value = IntegerField(verbose_name='Value')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return 'field:{0}, type:{1}, value:{2}'.format(self.field, self.count_type, self.value)


