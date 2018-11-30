from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    code = models.CharField(max_length=50, verbose_name='Code', unique=True, default='default')
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, verbose_name='Parent')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Declare(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', related_name='declares')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1, related_name='declares')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return str(self.member)


class RiceArea(models.Model):
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop', related_name='rice_areas')
    area = models.FloatField(null=True, verbose_name='Area')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return str(self.area)


class FallowTransfer(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', related_name='fallow_transfer')
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop', related_name='fallow_transfer')
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    period = models.CharField(max_length=1, null=True, verbose_name='Period')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}, {}, {}".format(self.member, self.crop, self.subsidy, self.period)


class TransferCrop(models.Model):
    declare = models.ForeignKey('fallow.Declare', on_delete=models.CASCADE, verbose_name='Declare', related_name='transfer_crops')
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop', related_name='transfer_crops')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}".format(self.rice_area, self.crop)
