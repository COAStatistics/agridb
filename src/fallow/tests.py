from django.test import TestCase
from django.core.management import call_command
from fallow.models import Crop, Declare, RiceArea
from household.models import Household, Member, Role


class CropTestCase(TestCase):

    def setUp(self):
        # load fixtures
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)

    def test_loaddata(self):
        crop_list = Crop.objects.all()
        self.assertEqual(len(crop_list), 6)

    def test_crop_delete(self):
        Crop.objects.filter(id=1).delete()
        crop_list = Crop.objects.filter(parent=1)
        self.assertEqual(len(crop_list), 0)
        self.assertEqual(Crop.objects.all().count(), 3)

    def test_crop_delete_all(self):
        Crop.objects.all().delete()
        self.assertEqual(len(Crop.objects.all()), 0)


class DeclareTestCase(TestCase):
    def setUp(self):
        # load fixtures
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/declare.yaml', verbosity=0)

    def test_declare_delete(self):
        print('delete one :')
        declare_list_before = Declare.objects.all()
        print('before delete count :', len(declare_list_before))
        Member.objects.get(id=1).delete()
        declare_list_after = Declare.objects.all()
        print('after delete count :', len(declare_list_after))
        self.assertEqual(len(declare_list_after), 2)

    def test_declare_delete_all(self):
        print('delete all :')
        declare_list_before = Declare.objects.all()
        print('before delete count :', len(declare_list_before))
        Member.objects.all().delete()
        declare_list_after = Declare.objects.all()
        print('after delete count :', len(declare_list_after))
        self.assertEqual(len(declare_list_after), 0)


class RiceAreaTestCase(TestCase):
    def setUp(self):
        # load fixtures
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/declare.yaml', verbosity=0)
        call_command('loaddata', 'tests/ricearea.yaml', verbosity=0)

    def test_rice_area_delete(self):
        print(RiceArea.objects.all())
        Declare.objects.get(id=1).delete()
        print(RiceArea.objects.all())
        self.assertEqual(len(RiceArea.objects.all()), 2)
        Crop.objects.get(id=2).delete()
        print(RiceArea.objects.all())
        self.assertEqual(len(RiceArea.objects.all()), 1)
