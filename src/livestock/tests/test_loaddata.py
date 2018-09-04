from django.test import TestCase
from django.core.management import call_command

from livestock import models


class YamlTest(TestCase):

    def setUp(self):
        print("-- load fixtures from Household --")
        call_command('loaddata', 'role.yaml', verbosity=0)
        call_command('loaddata', 'household.yaml', verbosity=0)
        call_command('loaddata', 'member.yaml', verbosity=0)
        print("-- load fixtures from Livestock --")
        call_command('loaddata', 'livestock.yaml', verbosity=0)
        call_command('loaddata', 'field.yaml', verbosity=0)
        call_command('loaddata', 'investigation.yaml', verbosity=0)
        call_command('loaddata', 'counttype.yaml', verbosity=0)
        call_command('loaddata', 'profile.yaml', verbosity=0)

    def test_loaddata(self):
        print("Start test loaddata")
        livestocks = models.Livestock.objects.all()
        fields = models.Field.objects.all()
        investigations = models.Investigation.objects.all()
        count_types = models.CountType.objects.all()
        profiles = models.Profile.objects.all()

        self.assertEqual(3, livestocks.count())
        self.assertEqual(2, fields.count())
        self.assertEqual(4, investigations.count())
        self.assertEqual(3, count_types.count())
        self.assertEqual(2, profiles.count())
