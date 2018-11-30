from django.db import models

# Create your models here.


class Household(models.Model):
    household_number = models.CharField(max_length=20, null=True, unique=True)
    address = models.CharField(max_length=255, null=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.household_number, self.address)


class Role(models.Model):
    name = models.CharField(max_length=20, null=True, unique=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    household = models.ForeignKey('household.Household', on_delete=models.CASCADE, related_name='members')
    role = models.ForeignKey('household.Role', on_delete=models.CASCADE, related_name='members')
    app_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, null=True)
    birth = models.DateField(null=True)
    code = models.PositiveIntegerField(null=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_id


class Year(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
