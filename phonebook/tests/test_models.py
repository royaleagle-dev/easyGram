from django.test import TestCase
from phonebook.models import Contact, ActivityLog
from django.utils import timezone

def create_contact(firstname, lastname, phone):
    return Contact.objects.create(firstname = firstname, lastname=lastname, phone=phone)

def create_log(activity):
    return ActivityLog.objects.create(activity=activity)

class TestContactModel(TestCase):
    
    def test_create_contact(self):
        contact = create_contact('Ayotunde', 'Okunubi', 'Olupamilerin')
        self.assertEqual(contact.__str__(), 'Ayotunde')

class TestActivityLogModel(TestCase):

    def test_create_activity_log(self):
        log = create_log(activity = 'Added New User: <Tompolo>')
        self.assertEqual(log.__str__(), 'Added New User: <Tompolo>')




