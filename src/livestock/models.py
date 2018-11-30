from django.db.models import (
    Model,
    CASCADE,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKey,
)

SEASON_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
]


class Livestock(Model):
    name = CharField(max_length=50, verbose_name='Name')
    code = CharField(max_length=12, verbose_name='Code', default='default')
    parent = ForeignKey('self', blank=True, null=True, default=None, on_delete=CASCADE, verbose_name='Parent')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

    def full_code(self):
        if self.parent:
            return self.parent.full_code() + self.code
        return self.code


class InvestigationType(Model):
    name = CharField(max_length=50, unique=True, verbose_name='Name')
    code = CharField(max_length=1, verbose_name='Code', default='Q')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Investigation(Model):
    type = ForeignKey('livestock.InvestigationType', null=True, on_delete=CASCADE, verbose_name='Investigation Type')
    year = IntegerField(verbose_name='Year')
    season = CharField(max_length=1, choices=SEASON_CHOICES, verbose_name='Season')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return 'year:{0}, season:{1}'.format(self.year, self.season)

    def full_season(self):
        if self.type:
            return self.type.code + self.season
        return self.season


class CountType(Model):
    name = CharField(max_length=50, unique=True, verbose_name='Name')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Field(Model):
    name = CharField(max_length=50, verbose_name='Name')
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member', related_name='fields')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Profile(Model):
    member = ForeignKey('household.Member', on_delete=CASCADE, verbose_name='Member', related_name='profiles')
    investigation = ForeignKey('livestock.Investigation', on_delete=CASCADE, verbose_name='Investigation', related_name='profiles')
    field = ForeignKey('livestock.Field', null=True, on_delete=CASCADE, verbose_name='Field', related_name='profiles')
    livestock = ForeignKey('livestock.Livestock', on_delete=CASCADE, verbose_name='Livestock', related_name='profiles')
    count_type = ForeignKey('livestock.CountType', on_delete=CASCADE, verbose_name='Count Type', related_name='profiles')
    value = IntegerField(verbose_name='Value')
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return 'field:{0}, type:{1}, value:{2}'.format(self.field, self.count_type, self.value)


