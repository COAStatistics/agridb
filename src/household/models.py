from django.db import models

# Create your models here.


class Household(models.Model):
    household_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} {}".format(self.household_number, self.address)


class Role(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    household = models.ForeignKey('household.Household', on_delete=models.CASCADE)
    role = models.ForeignKey('household.Role', on_delete=models.CASCADE)
    app_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True)
    birth = models.DateField(null=True)

    def __str__(self):
        return self.app_id
