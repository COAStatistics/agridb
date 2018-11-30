from django.db import models


class LandlordRetire(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', related_name='landlord_retires')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1, related_name='landlord_retires')
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class LandlordRent(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', related_name='landlord_rents')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1, related_name='landlord_rents')
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class TenantTransfer(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', related_name='tenant_transfers')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1, related_name='tenant_transfers')
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.subsidy)


class Tenant(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member', null=True, related_name='member_tenants')
    owner = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Landlord', null=True, related_name='owners_tenants')
    year = models.ForeignKey('household.Year', on_delete=models.CASCADE, verbose_name='Year', default=1)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    # class Meta:
    #     unique_together = ('member', 'owner', 'year')

    # def clean(self):
    #     from django.core.exceptions import ValidationError
    #     if Tenant.objects.filter(member=self.member, owner=self.owner, year=self.year).exists():
    #         raise ValidationError("1.{}\n2.{}\n3.{}".format(self.member, self.owner, self.year))

    def __str__(self):
        return "{}  {}  {}".format(self.year, self.member, self.owner)
