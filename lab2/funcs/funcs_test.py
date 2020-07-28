
import unittest
from funcs import f, g, hypotenuse, is_positive



class TestCases(unittest.TestCase):
    def test_f_1(self):
        self.assertEqual(f(2), 32)
        self.assertEqual(f(3), 69)

    def test_f_2(self):
        self.assertEqual(g(2, 2), 8)
        self.assertEqual(g(3, 3), 18)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(2, 3), 3.6055513)
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_is_positive(self):
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(-5))
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()                                                                                                            
