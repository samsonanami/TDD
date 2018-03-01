import unittest
from phone_book_app import PhoneBook

class PhoneAppTestCase(unittest.TestCase):
    def test_add_contact(self):
        phonebook = PhoneBook()
        response = phonebook.add_contacts("New Person","0732245565")
        self.assertEqual(response["Message"],"New contact added successfully")
    def test_view_contact(self):
        phonenebook = PhoneBook()
        response = phonenebook.view_contact("Samson Anami")
        self.assertEqual(response["Message"],"Contact view successful")
    def test_contact_not_found(self):
        phonebook = PhoneBook()
        response = phonebook.view_contact("Solomon Kalu")
        self.assertEqual(response["Message"],"Contact not found")
    def test_update_contact(self):
        phonebook = PhoneBook()
        response = phonebook.update_contact("Maina Charles","0712345678")
        self.assertEqual(response["Message"],"Contact updated successfully")
    def test_delete_contact(self):
        phonebook = PhoneBook()
        response = phonebook.delete_contact("Joel Nganga")
        self.assertEqual(response["Message"],"Contact deleted successfully")