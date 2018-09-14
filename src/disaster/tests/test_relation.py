from django.test import TestCase
from django.core.management import call_command
from disaster.models import (
    Disaster,
)


class DisasterTest(TestCase):
    def setUp(self):
        print("\n\nsetUp")
        # load fixtures

        print('load houshold')
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        print('load role')
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        print('load member')
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        print('load crop')
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        print('load disasterevent')
        call_command('loaddata', 'tests/disasterevent.yaml', verbosity=0)
        print('load disaster')
        call_command('loaddata', 'tests/disaster.yaml', verbosity=0)

    def test_delete_disasterevent(self):
        disaster_qs = Disaster.objects.filter(id=1)
        self.assertEqual(1, disaster_qs.count())
        # delete related object
        disaster_qs.first().event.delete()
        self.assertEqual(0, disaster_qs.count())

    def test_delete_member(self):
        disaster_qs = Disaster.objects.filter(id=1)
        self.assertEqual(1, disaster_qs.count())
        # delete related member object
        disaster_qs.first().member.delete()
        self.assertEqual(0, disaster_qs.count())

    def test_delete_crop(self):
        disaster_qs = Disaster.objects.filter(id=1)
        self.assertEqual(1, disaster_qs.count())
        # delete related crop object
        disaster_qs.first().crop.delete()
        self.assertEqual(0, disaster_qs.count())


