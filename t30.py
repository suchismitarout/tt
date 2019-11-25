some_string = "MOUTAIN2BEAUTIFUL8"
res = ''.join(filter(lambda x: x.isdigit(), some_string))
print(res)

import unittest

class Teststring(unittest.TestCase):
    def setUp(self):
        pass

    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_upper(self):
        self.assertEqual('best'.upper(), 'BEST')

    def test_lower(self):
        self.assertEqual('TEST'.lower(), 'test')

if __name__ == '__main__':
    unittest.main()