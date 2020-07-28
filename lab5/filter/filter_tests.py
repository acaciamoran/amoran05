# Name:
# Course:
# Instructor:
# Assignment:
# Term:

import unittest
import filter


class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)
    
    def test_are_positive_1(self):
        nums = [2, 4, 6, 8]
        positive = filter.are_positive(nums)
        self.assertListAlmostEqual(positive, [2, 4, 6, 8]) 
    def test_are_positive_2(self):
        nums = [1, -1, -3, -100]
        positive = filter.are_positive(nums)
        self.assertListAlmostEqual(positive, [1]) 

    def test_are_greater_than_n_1(self):
        nums = [1, -1, 0, -100]
        value = 2
        greater = filter.are_greater_than_n(nums, value)
        self.assertListAlmostEqual(greater, []) 
    def test_are_greater_than_n_2(self):
        nums = [1267, -2, 200, 100]
        value = 100
        greater = filter.are_greater_than_n(nums, value)
        self.assertListAlmostEqual(greater, [1267, 200]) 

    def test_are_divisible_by_n_1(self):
        nums = [10, -1, 0, -100]
        value = 5
        divisible = filter.are_divisible_by_n(nums, value)
        self.assertListAlmostEqual(divisible, [10, 0, -100]) 
    def test_are_divisible_by_n_2(self):
        nums = [9, -3, 300, 2]
        value = 3
        divisible = filter.are_divisible_by_n(nums, value)
        self.assertListAlmostEqual(divisible, [9, -3, 300]) 




# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
