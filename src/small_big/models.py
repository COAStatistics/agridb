from django.db import models


class LandlordRetire(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE)
    subsidy = models.IntegerField(null=True)


class LandlordRent(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE)
    subsidy = models.IntegerField(null=True)


class TenantTransfer(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE)
    subsidy = models.IntegerField(null=True)


class TenantList(models.Model):

    member = models.ForeignKey('household.Member', null=True, on_delete=models.CASCADE, related_name='tenant_list_member')
    owner = models.ForeignKey('household.Member', null=True, on_delete=models.CASCADE, related_name='tenant_list_owner')
