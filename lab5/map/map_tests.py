# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import map


class TestCases(unittest.TestCase):
        
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)
    
    def test_square_all_1(self):
        nums = [2, 4, 6, 8]
        squares = map.square_all(nums)
        self.assertListAlmostEqual(squares, [4, 16, 36, 64]) 
    def test_square_all_2(self):
        nums = [1, 0, 10, 7]
        squares = map.square_all(nums)
        self.assertListAlmostEqual(squares, [1, 0, 100, 49])

    def test_add_n_all_1(self):
        nums = [1, 2, 3, 4]
        value = 2
        add = map.add_n_all(nums, value)
        self.assertListAlmostEqual(add, [3, 4, 5, 6])
    def test_add_n_all_2(self):
        nums = [5, 0, 8, 3]
        value = 4
        add = map.add_n_all(nums, value)
        self.assertListAlmostEqual(add, [9, 4, 12, 7])


    def test_even_or_odd_all_1(self):
        nums = [2, 5, 8, 11]
        evens = map.even_or_odd_all(nums)
        self.assertListAlmostEqual(evens, [True, False, True, False])
    def test_even_or_odd_all_2(self):
        nums = [3, 3, 8, 11]
        evens = map.even_or_odd_all(nums)
        self.assertListAlmostEqual(evens, [False, False, True, False])


        


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
