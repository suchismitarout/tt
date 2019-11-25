import unittest

class Testcal(unittest.TestCase):
    def test_add(self):
        result = 5 + 5
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()


