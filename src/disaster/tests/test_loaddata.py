from django.test import TestCase
from django.core.management import call_command
from disaster import models


class DisasterTestCase(TestCase):

    def setUp(self):
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

    def test_loaddata(self):
        print("Start tests loaddata")
        disaster = models.Disaster.objects.all()
        disasterevent = models.DisasterEvent.objects.all()

        self.assertEqual(3, disaster.count())
        self.assertEqual(3, disasterevent.count())


