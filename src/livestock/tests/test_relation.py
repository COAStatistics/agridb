from django.test import TestCase
from django.core.management import call_command

from household.models import (
    Member,
)
from livestock.models import (
    Field,
    Profile,
    CountType,
    Investigation,
    Livestock,
)


class FieldRelationTest(TestCase):

    def setUp(self):
        print("Start test relation between livestock.Field and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'field.yaml', verbosity=0)

    def test_delete(self):
        field_qs = Field.objects.filter(id=1)
        self.assertEqual(1, field_qs.count())

        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, field_qs.count())


class ProfileRelationTest(TestCase):

    def setUp(self):
        print("Test Profile relation with livestock models")
        call_command('loaddata', 'role.yaml', verbosity=0)
        call_command('loaddata', 'household.yaml', verbosity=0)
        call_command('loaddata', 'member.yaml', verbosity=0)
        call_command('loaddata', 'livestock.yaml', verbosity=0)
        call_command('loaddata', 'field.yaml', verbosity=0)
        call_command('loaddata', 'investigation.yaml', verbosity=0)
        call_command('loaddata', 'counttype.yaml', verbosity=0)
        call_command('loaddata', 'profile.yaml', verbosity=0)

    def test_delete_investigation(self):
        profile_qs = Profile.objects.filter(id=1)
        self.assertEqual(1, profile_qs.count())

        # delete related object
        profile_qs.first().investigation.delete()

        self.assertEqual(0, profile_qs.count())

    def test_delete_field(self):
        profile_qs = Profile.objects.filter(id=1)
        self.assertEqual(1, profile_qs.count())

        # delete related object
        profile_qs.first().field.delete()

        self.assertEqual(0, profile_qs.count())

    def test_delete_count_type(self):
        profile_qs = Profile.objects.filter(id=1)
        self.assertEqual(1, profile_qs.count())

        # delete related object
        profile_qs.first().count_type.delete()

        self.assertEqual(0, profile_qs.count())

    def test_delete_livestock(self):
        profile_qs = Profile.objects.filter(id=1)
        self.assertEqual(1, profile_qs.count())

        # delete related object
        profile_qs.first().livestock.delete()

        self.assertEqual(0, profile_qs.count())


class LivestockRelationTest(TestCase):

    def setUp(self):
        print("Test Livestock relation with itself")
        call_command('loaddata', 'livestock.yaml', verbosity=0)

    def test_delete_parent(self):
        livestock_qs = Livestock.objects.filter(id=2)
        self.assertEqual(1, livestock_qs.count())

        # delete related object
        livestock_qs.first().parent.delete()

        self.assertEqual(0, livestock_qs.count())


