import unittest
import list_comp
from objects import *


class TestCases(unittest.TestCase):
    
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_distance_all_1(self):
        points = [Point(5.0, 3.0), Point(4.0, 6.0)]
        distances = list_comp.distance_all(points)
        self.assertListAlmostEqual(distances, [5.830951894, 7.211102550927])
    
    def test_are_in_first_quadrant_1(self):
        points = [Point(5.0, 3.0), Point(4.0, 6.0)]
        good_points = list_comp.are_in_first_quadrant(points)
        self.assertListAlmostEqual(good_points, [Point(5.0, 3.0), Point(4.0, 6.0)])
    def test_are_in_first_quadrant_2(self):
        points = [Point(5.0, -3.0), Point(4.0, 6.0)]
        good_points = list_comp.are_in_first_quadrant(points)
        self.assertListAlmostEqual(good_points, [Point(4.0, 6.0)])

    def test_are_in_first_quadrant_3(self):
        points = [Point(5.0, 3.0), Point(-4.0, 6.0)]
        good_points = list_comp.are_in_first_quadrant(points)
        self.assertListAlmostEqual(good_points, [Point(5.0, 3.0)])

if __name__ == '__main__':
    unittest.main()
