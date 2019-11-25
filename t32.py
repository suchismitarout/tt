import unittest
class Testum(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual((3*4), 12)

    def test_multiply1(self):
        self.assertEqual(('a'*3), 'aaa')


if __name__ == '__main__':
    unittest.main()
