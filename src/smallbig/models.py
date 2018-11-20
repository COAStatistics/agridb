from django.db import models


class LandlordRetire(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class LandlordRent(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class TenantTransfer(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class Tenant(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, related_name='tenant_member_set', verbose_name='Member')
    owner = models.ForeignKey('household.Member', on_delete=models.CASCADE, related_name='tenant_owner_set', verbose_name='Landlord')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.owner)
