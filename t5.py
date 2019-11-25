import unittest
from t4 import *


class Testemployee(unittest.Testcase):
    def test_email(self):
        emp1 = Employee("john", "snow", 50000)
        emp2 = Employee("sansa", "stark", 60000)

        self.assertEqual(emp1.get_email, "john.snow@gmail.com")
        self.assertEqual(emp2.get_email, "sansa.stark@gmail.com")


if __name__ == '__main__':
    unittest.main()

