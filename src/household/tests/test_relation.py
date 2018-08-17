from django.test import TestCase
from django.core.management import call_command

from household import models


class HouseholdRelationTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)

    def test_delete(self):
        print("Start test Household relation")
        household = models.Household.objects.all()
        household.delete()
        member = models.Member.objects.all()
        self.assertEqual(0, member.count())


class RoleRelationTest(TestCase):

    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)

    def test_delete(self):
        print("Start test Role relation")
        role = models.Role.objects.all()
        role.delete()
        member = models.Member.objects.all()
        self.assertEqual(0, member.count())
