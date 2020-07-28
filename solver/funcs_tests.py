# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 2
# Term:         Spring 2017
from solver_funcs import *
import unittest

class TestCases(unittest.TestCase):

    def test_check_valid_with_invalid(self):
        puzzle = [[1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

        cages = [[9,  3, 0,  5,  6],
               [7,  2, 1,  2],
               [10, 3, 3,  8,  13],
               [14, 4, 4,  9,  14, 19],
               [3,  1, 7],
               [8,  3, 10, 11, 16],
               [13, 4, 12, 17, 21, 22],
               [5,  2, 15, 20],
               [6,  3, 18, 23, 24]]

        self.assertFalse(check_valid(puzzle, cages))



    def test_check_row_valid_1(self):
        row = [1, 2, 3, 4]
        self.assertTrue(check_row_valid(row))
    
    def test_check_row_valid_2(self):
        row = [1, 1, 3, 4]
        self.assertFalse(check_row_valid(row))
    
    def test_check_row_valid_3(self):
        row = [1, 2, 1, 2]
        self.assertFalse(check_row_valid(row))
    
    def test_check_row_valid_4(self):
        row = [1, 4, 5, 2]
        self.assertTrue(check_row_valid(row))


    
    
    def test_check_rows_valid_1(self):
        puzzle = [[1, 1, 5, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [1, 7, 5, 0, 3],
                [0, 2, 9, 3, 8]]
        self.assertFalse(check_rows_valid(puzzle))
    
    def test_check_rows_valid_2(self):
        puzzle = [[1, 2, 5, 0, 6],
                [2, 7, 6, 3, 0],
                [0, 2, 1, 4, 7],
                [1, 8, 5, 0, 3],
                [0, 2, 9, 4, 8]]
        self.assertTrue(check_rows_valid(puzzle))
    
    def test_check_rows_valid_3(self):
        puzzle = [[1, 2, 5, 0, 6],
                [2, 7, 5, 3, 0],
                [0, 2, 8, 4, 7],
                [7, 7, 7, 7, 3],
                [0, 2, 9, 3, 8]]
        self.assertFalse(check_rows_valid(puzzle))

    
    
    
    def test_column1_1(self):
        puzzle = [[1, 2, 5, 0, 6],
                [2, 7, 5, 3, 0],
                [0, 2, 8, 4, 7],
                [7, 7, 7, 7, 3],
                [0, 2, 9, 3, 8]]
        self.assertEqual(column1(puzzle), [[1, 2, 0, 7, 0], 
                                        [2, 7, 2, 7, 2], 
                                        [5, 5, 8, 7, 9],
                                        [0, 3, 4, 7, 3],
                                        [6, 0, 7, 3, 8]])
    def test_column1_2(self):
        puzzle = [[3, 4, 6, 2, 3],
                [2, 7, 5, 3, 0],
                [0, 2, 8, 4, 7],
                [7, 7, 7, 7, 3],
                [0, 2, 9, 3, 8]]
        self.assertEqual(column1(puzzle), [[3, 2, 0, 7, 0], 
                                        [4, 7, 2, 7, 2], 
                                        [6, 5, 8, 7, 9],
                                        [2, 3, 4, 7, 3],
                                        [3, 0, 7, 3, 8]])
    def test_column1_3(self):
        puzzle = [[3, 4, 6, 2, 3],
                [2, 7, 5, 3, 0],
                [0, 2, 8, 4, 7],
                [7, 3, 7, 7, 3],
                [1, 2, 9, 3, 8]]
        self.assertEqual(column1(puzzle), [[3, 2, 0, 7, 1], 
                                        [4, 7, 2, 3, 2], 
                                        [6, 5, 8, 7, 9],
                                        [2, 3, 4, 7, 3],
                                        [3, 0, 7, 3, 8]])
    
    
    
    
    def test_check_column_valid_1(self):
        col = [1, 1, 5, 0, 6]
        self.assertFalse(check_column_valid(col))
    
    def test_check_column_valid_2(self):
        col = [2, 3, 5, 0, 6]
        self.assertTrue(check_column_valid(col))
    
    def test_check_column_valid_3(self):
        col = [1, 9, 7, 3, 5]
        self.assertTrue(check_column_valid(col))

    
    
    def test_check_columns_valid_1(self):
        puzzle = [[1, 1, 5, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [1, 7, 5, 0, 3],
                [0, 2, 9, 3, 8]]
        self.assertFalse(check_columns_valid(puzzle))
    
    def test_check_columns_valid_2(self):
        puzzle = [[1, 1, 5, 7, 6],
                [2, 7, 4, 3, 0],
                [4, 2, 8, 4, 7],
                [9, 3, 0, 0, 3],
                [0, 5, 9, 2, 8]]
        self.assertTrue(check_columns_valid(puzzle))
    
    def test_check_columns_valid_3(self):
        puzzle = [[1, 1, 5, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 1, 8]]
        self.assertTrue(check_columns_valid(puzzle))

    
    
    def test_get_cage_value_1(self):
        puzzle = [[1, 1, 5, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 1, 8]]

        cage = [9, 3, 8, 1, 2]
        self.assertEqual(get_cage_value(puzzle, cage), (9, 0))

    def test_get_cage_value_2(self):
        puzzle = [[1, 1, 5, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 1, 8]]
        cage = [6, 2, 3, 4]
        self.assertEqual(get_cage_value(puzzle, cage), (6, 1))
    
    def test_get_cage_value_3(self):
        puzzle = [[1, 1, 5, 1, 6],
                [2, 7, 4, 3, 0],
                [0, 2, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 1, 8]]
        cage = [7, 2, 3, 4]
        self.assertEqual(get_cage_value(puzzle, cage), (7, 0))

    def test_get_cage_value_4(self):
        puzzle = [[1, 1, 4, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cage = [21, 5, 0, 2, 4, 6, 8]
        self.assertEqual(get_cage_value(puzzle, cage), (21, 0))

    
    
    def test_check_cage_valid_1(self):
        puzzle = [[1, 1, 4, 3, 6],
                [2, 7, 4, 3, 2],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cage = [21, 5, 0, 2, 4, 6, 8]
        self.assertTrue(check_cage_valid(puzzle, cage))
    
    def test_check_cage_valid_2(self):
        puzzle = [[1, 1, 4, 3, 6],
                [2, 7, 4, 3, 2],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cage = [20, 5, 0, 2, 4, 6, 8]
        self.assertFalse(check_cage_valid(puzzle, cage))

    def test_check_cage_valid_3(self):
        puzzle = [[1, 1, 4, 2, 6],
                [2, 7, 4, 3, 3],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
       
        cage = [8, 4, 0, 1, 2, 3]
        self.assertTrue(check_cage_valid(puzzle, cage))
    
    def test_check_cage_valid_4(self):
        puzzle = [[0, 1, 4, 2, 6],
                [2, 7, 4, 3, 3],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
       
        cage = [8, 4, 0, 1, 2, 3]
        self.assertTrue(check_cage_valid(puzzle, cage))
    
    def test_check_cage_valid_5(self):
        puzzle = [[1, 1, 4, 2, 6],
                [2, 7, 4, 3, 3],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
       
        cage = [9, 4, 0, 1, 2, 3]
        self.assertFalse(check_cage_valid(puzzle, cage))


   
   
    def test_check_cages_valid_1(self):
        puzzle = [[1, 1, 4, 1, 6],
                [2, 7, 4, 3, 0],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cages = [[7, 4, 0, 1, 2, 3],
                [25, 5, 7, 11, 4, 6, 8],
                [17, 3, 22, 5, 18]]
        self.assertTrue(check_cages_valid(puzzle, cages))

    def test_check_cages_valid_2(self):
        puzzle = [[1, 1, 4, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cages = [[6, 4, 0, 1, 2, 3],
                [20, 5, 0, 2, 4, 6, 8]]
        self.assertFalse(check_cages_valid(puzzle, cages))
   
    def test_check_cages_valid_3(self):
        puzzle = [[1, 1, 4, 0, 6],
                [2, 7, 4, 3, 0],
                [0, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cages = [[6, 4, 0, 1, 2, 3],
                [21, 5, 0, 2, 4, 6, 8],
                [2, 2, 2, 1]]
        self.assertFalse(check_cages_valid(puzzle, cages))
    
    def test_check_cages_valid_4(self):
        puzzle = [[1, 1, 4, 2, 6],
                [2, 7, 4, 3, 1],
                [2, 5, 8, 4, 7],
                [3, 4, 2, 6, 3],
                [4, 5, 9, 2, 8]]
        cages = [[13, 4, 4, 1, 2, 3],
                [20, 5, 9, 11, 13, 6, 8],
                [9, 2, 10, 14],
                [19, 3, 24, 23, 22]]
        self.assertTrue(check_cages_valid(puzzle, cages))

    
    
    def test_check_valid_1(self):
        puzzle = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        cages =  [[9, 3, 0, 5, 6],
                [7, 2, 1, 2],
                [10, 3, 3, 8, 13],
                [14, 4, 4, 9, 14, 19],
                [3, 1, 7],
                [8, 3, 10, 11, 16],
                [13, 4, 12, 17, 21, 22],
                [5, 2, 15, 20],
                [6, 3, 18, 23, 24]]
        self.assertTrue(check_valid(puzzle, cages))
   
    def test_check_valid_2(self):
        puzzle = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        cages =  [[9, 3, 0, 5, 6],
                [7, 2, 1, 2],
                [10, 3, 3, 8, 13],
                [14, 4, 4, 9, 14, 19],
                [3, 1, 7],
                [8, 3, 10, 11, 16],
                [13, 4, 12, 17, 21, 22],
                [5, 2, 15, 20],
                [6, 3, 18, 23, 20]]
        self.assertFalse(check_valid(puzzle, cages))

    def test_check_valid_3(self):
        puzzle = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        cages =  [[9, 3, 0, 5, 6],
                [7, 2, 1, 2],
                [10, 3, 3, 8, 13],
                [14, 4, 4, 9, 14, 19],
                [3, 1, 7],
                [8, 3, 10, 11, 16],
                [13, 4, 12, 17, 21, 22],
                [5, 2, 15, 20],
                [5, 3, 18, 23, 24]]
        self.assertFalse(check_valid(puzzle, cages))

    def test_check_valid_4(self):
        puzzle = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [5, 3, 5, 2, 1]]
        cages =  [[9, 3, 0, 5, 6],
                [7, 2, 1, 2],
                [10, 3, 3, 8, 13],
                [14, 4, 4, 9, 14, 19],
                [3, 1, 7],
                [8, 3, 10, 11, 16],
                [13, 4, 12, 17, 21, 22],
                [5, 2, 15, 20],
                [6, 3, 18, 23, 24]]
        self.assertFalse(check_valid(puzzle, cages))

    def test_check_valid_5(self):
        puzzle = [[3, 5, 2, 1, 4],
                [5, 1, 3, 3, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        cages =  [[9, 3, 0, 5, 6],
                [7, 2, 1, 2],
                [10, 3, 3, 8, 13],
                [14, 4, 4, 9, 14, 19],
                [3, 1, 7],
                [8, 3, 10, 11, 16],
                [13, 4, 12, 17, 21, 22],
                [5, 2, 15, 20],
                [6, 3, 18, 23, 24]]
        self.assertFalse(check_valid(puzzle, cages))
if __name__ == '__main__':
   unittest.main()
