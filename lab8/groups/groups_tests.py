import unittest
from groups import *


class TestCases(unittest.TestCase):
   
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_groups_of_3(self):
        lst = [1, 3, 5, 6, 3, 8, 6, 1, 5]
        group_lst = [[1, 3, 5], [6, 3, 8], [6, 1, 5]]
        self.assertListAlmostEqual(groups_of_3(lst, 3), group_lst)

    def test_groups_of_3_2(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        group_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]
        self.assertListAlmostEqual(groups_of_3(lst, 3), group_lst)


if __name__ == '__main__':
    unittest.main()
