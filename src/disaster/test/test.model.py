from django.test import TestCase
from django.core.management import call_command
from disaster import models

class DisasterEvent(TestCase):
    def sepUp(self):
        print("\n\nsetUp")
    def test_model(self):
        print("Start test DisasterEvent model")
        name = 'xxw颱風'
        models.DisasterEvent.objects.create(name=name)
        self.assertEqual(1, models.DisasterEvent.objects.all().count())

class Disaster(TestCase):

    def setUp(self):
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/disasterevent.yaml', verbosity=0)

    def test_model(self):
        print("Start test Disaster model")
        member = models.Member.objects.first()
        event = models.DisasterEvent.objects.first()
        crop = models.Crop.objects.first()
        area = '35'
        subsidy = '2500'
        models.Disaster.objects.create(member=member, event=event, crop=crop, area=area, subsidy=subsidy)

