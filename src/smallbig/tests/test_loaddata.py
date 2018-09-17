from django.test import TestCase
from django.core.management import call_command
from smallbig import models

class YamlTest(TestCase):
    def setUp(self):
        print("-- load fixtures from household --")
        call_command('loaddata', 'role.yaml', verbosity=0)
        call_command('loaddata', 'household.yaml', verbosity=0)
        call_command('loaddata', 'member.yaml', verbosity=0)
        print("-- load fixtures from smallbig --")
        call_command('loaddata', 'landlordretire.yaml', verbosity=0)
        call_command('loaddata', 'landlordrent.yaml', verbosity=0)
        call_command('loaddata', 'tenanttransfer.yaml', verbosity=0)
        call_command('loaddata', 'tenant.yaml', verbosity=0)

    def test_loaddata(self):
        print("Start test loaddata")
        landlordretire = models.LandlordRetire.objects.all()
        landlordrent = models.LandlordRent.objects.all()
        tenanttransfer = models.TenantTransfer.objects.all()
        tenant = models.Tenant.objects.all()
        print('landlordretire.count() =', landlordretire.count())
        self.assertEqual(3, landlordretire.count())
        print('landlordrent.count() =', landlordrent.count())
        self.assertEqual(3, landlordrent.count())
        print('tenanttransfer.count() =', tenanttransfer.count())
        self.assertEqual(3, tenanttransfer.count())
        print('tenant.count() =', tenant.count())
        self.assertEqual(1, tenant.count())