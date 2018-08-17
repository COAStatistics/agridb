from django.test import TestCase
from django.core.management import call_command
from fallow.models import Crop


class ModelTestCase(TestCase):

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
