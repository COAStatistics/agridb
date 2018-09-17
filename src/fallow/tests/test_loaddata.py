from django.test import TestCase
from django.core.management import call_command
from fallow import models


class YamlTest(TestCase):
    def setUp(self):
        print("-- load fixtures from household --")
        call_command('loaddata', 'role.yaml', verbosity=0)
        call_command('loaddata', 'household.yaml', verbosity=0)
        call_command('loaddata', 'member.yaml', verbosity=0)
        print("-- load fixtures from fallow --")
        call_command('loaddata', 'crop.yaml', verbosity=0)
        call_command('loaddata', 'declare.yaml', verbosity=0)
        call_command('loaddata', 'ricearea.yaml', verbosity=0)
        call_command('loaddata', 'fallowtransfer.yaml', verbosity=0)
        call_command('loaddata', 'transfercrop.yaml', verbosity=0)

    def test_loaddata(self):
        print("Start test loaddata")
        crop = models.Crop.objects.all()
        declare = models.Declare.objects.all()
        ricearea = models.RiceArea.objects.all()
        fallowtransfer = models.FallowTransfer.objects.all()
        transfercrop = models.TransferCrop.objects.all()
        print('crop.count() =', crop.count())
        self.assertEqual(6, crop.count())
        print('declare.count() =', declare.count())
        self.assertEqual(3, declare.count())
        print('ricearea.count() =', ricearea.count())
        self.assertEqual(3, ricearea.count())
        print('fallowtransfer.count() =', fallowtransfer.count())
        self.assertEqual(3, fallowtransfer.count())
        print('transfercrop.count() =', transfercrop.count())
        self.assertEqual(3, transfercrop.count())