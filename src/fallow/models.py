from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=50, null=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Declare(models.Model):
    member = models.ForeignKey('household.Member', null=True, on_delete=models.CASCADE)


class RiceArea(models.Model):
    declare = models.ForeignKey('fallow.Declare', null=True, on_delete=models.CASCADE)
    crop = models.ForeignKey('fallow.Crop', null=True, on_delete=models.CASCADE)
    area = models.FloatField(null=True)


class FallowTransfer(models.Model):
    member = models.ForeignKey('household.Member', null=True, on_delete=models.CASCADE)
    crop = models.ForeignKey('fallow.Crop', null=True, on_delete=models.CASCADE)
    subsidy = models.IntegerField(null=True)
    period = models.CharField(max_length=1, null=True)


class TransferCrop(models.Model):
    rice_area = models.ForeignKey('fallow.RiceArea', null=True, on_delete=models.CASCADE)
    crop = models.ForeignKey('fallow.Crop', null=True, on_delete=models.CASCADE)
