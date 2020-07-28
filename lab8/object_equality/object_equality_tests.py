import unittest
from objects import *
import utility


class TestCases(unittest.TestCase):

    def test_equality_1(self):
        p1 = Point(3.7, 6.8)
        p2 = Point(3.7, 6.8)
        self.assertEqual(p1.x, p2.x)
        self.assertEqual(p1.y, p2.y)
    
    def test_equality_2(self):
        p1 = Point(3.5, 6.8)
        p2 = Point(3.7, 6.8)
        self.assertNotEqual(p1.x, p2.x)
        self.assertEqual(p1.y, p2.y)

if __name__ == '__main__':
    unittest.main()
