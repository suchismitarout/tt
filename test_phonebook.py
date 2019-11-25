from phonebook import Phonebook
import unittest


class PhonebookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "123456")
        number = phonebook.lookup("Bob")
        self.assertEqual("123456", number)
