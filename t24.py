import unittest

class Testsum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual((sum(1, 2, 2)), "should equals to 6")
    def test_sum1(self):
        self.assertEqual((sum(1, 2, 3)), "should equals to 6")
if __name__ =='__main__':
    unittest.main()