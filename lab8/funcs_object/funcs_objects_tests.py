import unittest
from objects import *
import objects
from funcs_objects import *


class TestCases(unittest.TestCase):

    def test_point_1(self):
        pt1 = objects.Point(1.2, 2.5)
        self.assertEqual(pt1.x, 1.2)
        self.assertEqual(pt1.y, 2.5)

    def test_point_2(self):
        pt1 = objects.Point(5.0, 7.0)
        self.assertEqual(pt1.x, 5.0)
        self.assertEqual(pt1.y, 7.0)


    def test_distance_1(self):
        p1 = Point(5.0, 3.0)
        p2 = Point(4.0, 6.0)
        self.assertAlmostEqual(distance(p1, p2), 3.1622777)

    def test_distance_2(self):
        p3 = Point(3.0, 7.0)
        p4 = Point(2.0, 5.0)
        self.assertAlmostEqual(distance(p3, p4), 2.2360680)

    def test_circles_overlap_1(self):
        circle1 = Point(3.0, 5.0)
        circle2 = Point(4.0, 6.0)
        self.assertTrue(circles_overlap(circle1, circle2, 5.0, 3.0))

    def test_circles_overlap_2(self):
        circle3 = Point(5.0, 6.0)
        circle4 = Point(8.0, 7.0)
        self.assertFalse(circles_overlap(circle3, circle4, 1.0, 2.0))

if __name__ == '__main__':
    unittest.main()
