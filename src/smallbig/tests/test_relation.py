from django.test import TestCase
from django.core.management import call_command
from household.models import Member
from smallbig import models


class LandlordRetireRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between smallbig.LandlordRetire and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/landlordretire.yaml', verbosity=0)

    def test_delete(self):
        landlordretire_qs = models.LandlordRetire.objects.filter(id=1)
        self.assertEqual(1, landlordretire_qs.count())

        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, landlordretire_qs.count())


class LandlordRentRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between smallbig.LandlordRent and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/landlordrent.yaml', verbosity=0)

    def test_delete(self):
        landlordrent_qs = models.LandlordRent.objects.filter(id=1)
        self.assertEqual(1, landlordrent_qs.count())

        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, landlordrent_qs.count())


class TenantTransferRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between smallbig.TenantTransfer and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/tenanttransfer.yaml', verbosity=0)

    def test_delete(self):
        tenanttransfer_qs = models.TenantTransfer.objects.filter(id=1)
        self.assertEqual(1, tenanttransfer_qs.count())

        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, tenanttransfer_qs.count())


class TenantRelationTest(TestCase):
    def setUp(self):
        print("Start test relation between smallbig.Tenant and household.Member")
        call_command('loaddata', 'tests/role.yaml', verbosity=0)
        call_command('loaddata', 'tests/household.yaml', verbosity=0)
        call_command('loaddata', 'tests/member.yaml', verbosity=0)
        call_command('loaddata', 'tests/tenant.yaml', verbosity=0)

    def test_delete(self):
        tenant_qs = models.Tenant.objects.filter(id=1)
        self.assertEqual(1, tenant_qs.count())

        member = Member.objects.get(id=1)
        member.delete()
        self.assertEqual(0, tenant_qs.count())