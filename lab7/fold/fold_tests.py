import unittest
from fold import *


class TestCases(unittest.TestCase):

    def test_sum_1(self):
        list1 = [ 2, 3 , 4, 5]
        self.assertEqual(sum(list1), 14)
    
    def test_sum_2(self):
        list1 = []
        self.assertEqual(sum(list1), 0)
    
    def test_sum_3(self):
        list1 = [ 6, 3 , 4, 4]
        self.assertEqual(sum(list1), 17)
    
    def test_sum_4(self):
        list1 = [ 2, 3 , 3, 5]
        self.assertEqual(sum(list1), 13)
    
    def test_sum_5(self):
        list1 = [ 6, 3 , 4, 2]
        self.assertEqual(sum(list1), 15)


    def test_index_of_smallest_1(self):
        list1 = [6, 5, 2, 2, 3]
        self.assertEqual(index_of_smallest(list1), 2)

    def test_index_of_smallest_2(self):
        list1 = [6, 0, 2, 2, 3]
        self.assertEqual(index_of_smallest(list1), 1)
    def test_index_of_smallest_3(self):
        list1 = []
        self.assertEqual(index_of_smallest(list1), -1)
    def test_index_of_smallest_4(self):
        list1 = [6, 4, 2, 2, 1]
        self.assertEqual(index_of_smallest(list1), 4)
    def test_index_of_smallest_5(self):
        list1 = [6, 0, 2, 3, 3]
        self.assertEqual(index_of_smallest(list1), 1)
    def test_index_of_smallest_6(self):
        list1 = [1, 5, 2, 2, 3]
        self.assertEqual(index_of_smallest(list1), 0)









# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

