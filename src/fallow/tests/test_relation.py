from django.test import TestCase
from django.core.management import call_command
from household.models import Member
from fallow import models


class CropRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between fallow.Crop and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)

    def test_delete(self):
        crop_qs = models.Crop.objects.all()
        self.assertEqual(6, crop_qs.count())

        member = models.Crop.objects.get(id=1)
        member.delete()
        self.assertEqual(3, crop_qs.count())


class DeclareRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between fallow.Declare and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/declare.yaml', verbosity=0)

    def test_delete(self):
        declare_qs = models.Declare.objects.filter(id=1)
        self.assertEqual(1, declare_qs.count())
        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, declare_qs.count())


class RiceAreaRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between fallow.RiceArea and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/declare.yaml', verbosity=0)
        call_command('loaddata', 'tests/ricearea.yaml', verbosity=0)

    def test_delete(self):
        ricearea_qs = models.RiceArea.objects.filter(id=1)
        self.assertEqual(1, ricearea_qs.count())
        declare = models.Declare.objects.get(id=1)
        declare.delete()
        self.assertEqual(0, ricearea_qs.count())


class FallowTransferRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between fallow.FallowTransfer and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/fallowtransfer.yaml', verbosity=0)

    def test_delete(self):
        fallowtransfer_qs = models.FallowTransfer.objects.filter(id=1)
        self.assertEqual(1, fallowtransfer_qs.count())
        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, fallowtransfer_qs.count())


class TransferCropRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between fallow.TransferCrop and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/crop.yaml', verbosity=0)
        call_command('loaddata', 'tests/declare.yaml', verbosity=0)
        call_command('loaddata', 'tests/ricearea.yaml', verbosity=0)
        call_command('loaddata', 'tests/transfercrop.yaml', verbosity=0)

    def test_delete(self):
        transfercrop_qs = models.TransferCrop.objects.filter(id=1)
        self.assertEqual(1, transfercrop_qs.count())
        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, transfercrop_qs.count())
