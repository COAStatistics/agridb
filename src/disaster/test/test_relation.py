from django.test import TestCase
from django.core.management import call_command
from disaster import models

class DisasterTest(TestCase):
    def setUp(self):
        print("\n\nsetUp")
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/disasterevent.yaml', verbosity=0)
        call_command('loaddata', 'tests/disaster.yaml', verbosuty=0)

    def test_delete(self):
        print("Start test Disaster relation")
        household = models.Household.objects.all()
        household.delete()
        member = models.Member.objects.all()
        crop = models.Crop.objects.all()
        disasterevent = models.Disasterevent.objects.all()
        disaster = models.Disaster.objects.all()
        self.assertEqual(0, member.count())
