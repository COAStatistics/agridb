from django.test import TestCase
from django.core.management import call_command
from welfare import models  # import welfare app


class YamlTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/elderlyallowance.yaml', verbosity=0)
        call_command('loaddata', 'tests/farmerinsurance.yaml', verbosity=0)
        call_command('loaddata', 'tests/scholarship.yaml', verbosity=0)

    def test_loaddata(self):
        print("Start test loaddata")
        elderlyallowance = models.ElderlyAllowance.objects.all()
        farmerinsurance = models.FarmerInsurance.objects.all()
        scholarship = models.Scholarship.objects.all()

        self.assertEqual(3, elderlyallowance.count())
        self.assertEqual(6, farmerinsurance.count())
        self.assertEqual(9, scholarship.count())
