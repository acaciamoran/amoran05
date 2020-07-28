# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    # Example test case.
    def test_poly_add_1(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

    def test_poly_add_2(self):
        poly1 = [2, 2, 2]
        poly2 = [4, 4, 4]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [6, 6, 6])
    
    def test_poly_mult2_1(self):
        poly1 = [2, 4, 1]
        poly2 = [2, 4, 1]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [4, 16, 20, 8, 1])
    
    def test_poly_mult2_2(self):
        poly1 = [5, 2, 1]
        poly2 = [6, 7, 1]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [30, 47, 25, 9, 1])


if __name__ == '__main__':
    unittest.main()
