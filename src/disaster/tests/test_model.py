from django.test import TestCase
from django.core.management import call_command
from disaster.models import (
    DisasterEvent,
    Disaster,
)
from household.models import (
    Member,
)
from fallow.models import (
    Crop,
)


class DisasterEventTest(TestCase):
    def sepUp(self):
        print("\n\nsetUp")

    def test_model(self):
        print("Start tests DisasterEvent model")
        name = 'xxw颱風'
        DisasterEvent.objects.create(name=name)
        self.assertEqual(1, DisasterEvent.objects.all().count())


class DisasterTest(TestCase):

    def setUp(self):
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/disasterevent.yaml', verbosity=0)

    def test_model(self):
        print("Start tests Disaster model")
        member = Member.objects.first()
        event = DisasterEvent.objects.first()
        crop = Crop.objects.first()
        area = 35
        subsidy = 2500
        Disaster.objects.create(member=member, event=event, crop=crop, area=area, subsidy=subsidy)

        qs = Disaster.objects.filter(member=member, event=event, crop=crop, area=area, subsidy=subsidy)
        self.assertEqual(1, qs.count())

        self.assertEqual(area, qs.first().area)
