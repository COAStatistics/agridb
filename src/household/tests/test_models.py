from django.test import TestCase
from django.core.management import call_command

from household import models

# Create your tests here.


class HouseholdTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")

    def test_model(self):
        print("Start test Household model")
        household_number = '60001526489'
        address = "台北市中正區南海路37號"
        models.Household.objects.create(household_number=household_number, address=address)
        self.assertEqual(1, models.Household.objects.all().count())


class RoleTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")

    def test_model(self):
        print("Start test Role model")
        name = '測試測試'
        models.Role.objects.create(name=name)
        self.assertEqual(1, models.Role.objects.all().count())


class MemberTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)

    def test_model(self):
        print("Start test Member model")
        household = models.Household.objects.first()
        role = models.Role.objects.first()
        app_id = 'A1234567891'
        name = '鋼鐵人'
        birth = '1911-01-01'
        models.Member.objects.create(household=household, role=role, app_id=app_id, name=name, birth=birth)
        self.assertEqual(1, models.Member.objects.all().count())
