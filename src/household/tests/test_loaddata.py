from django.test import TestCase
from django.core.management import call_command

from household import models


class YamlTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)

    def test_loaddata(self):
        print("Start test loaddata")
        role = models.Role.objects.all()
        household = models.Household.objects.all()
        member = models.Member.objects.all()

        self.assertEqual(9, role.count())
        self.assertEqual(3, household.count())
        self.assertEqual(10, member.count())
