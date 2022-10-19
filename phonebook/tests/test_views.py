from django.test import TestCase
from phonebook.models import Contact, ActivityLog
from django.utils import timezone
from django.urls import reverse

def create_contact(firstname, lastname, phone):
    return Contact.objects.create(firstname = firstname, lastname=lastname, phone=phone)

class TestIndexView(TestCase):

    def test_successful_index_page_load(self):
        response = self.client.get(reverse('phonebook:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_contacts_available(self):
        response = self.client.get(reverse('phonebook:index'))
        self.assertQuerysetEqual(response.context['contacts'], [])

    def test_trashed_contacts(self):
        response = self.client.get(reverse('phonebook:trash'))
        contact1 = create_contact('Ayotunde', 'Okunubi', '09086756523')
        contact2 = create_contact('Olaoluwapo', 'Okunubi', '09086756523')
        contact3  = create_contact('Adebisi', 'Okunubi', '09086756523')
        contact1.trashed=True; contact1.save()
        contact3.trashed=True; contact3.save()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['contacts'], [contact1, contact3])

    def test_add_new_contact(self):
        url = reverse('phonebook:index')
        contact_data = {
            'firstname': 'Ayotunde',
            'lastname' : 'Okunubi',
            'phone' : '09023458745',
            'email': 'ay@gmail.com',
        }
        response = self.client.post(url, contact_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"status": "success", "message": "Contact added successfully"}')
    
    def test_add_new_contact_error(self):
        url = reverse('phonebook:index')
        contact_data = {
            'firstname': '',
            'lastname' : 'Okunubi',
            'phone' : '09023458745',
            'email': 'ay@gmail.com',
        }
        response = self.client.post(url, contact_data)
        self.assertEqual(response.content, b'{"status": "warning", "message": "One or more errors occured, Contact cannot be added"}'
)


class TestTrashedView(TestCase):

    def test_trashed_view(self):
        pass

    def test_contact_not_exist(self):
        pass


class TestActivityLogView(TestCase):

    def test_activity_log_available(self):
        pass

    def test_activity_log_empty(self):
        pass