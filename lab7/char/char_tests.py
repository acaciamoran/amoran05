import unittest
from char import *


class TestChar(unittest.TestCase):

    def test_is_lower_101_1(self):
        self.assertTrue(is_lower_101("n"))
    def test_is_lower_101_2(self):
        self.assertFalse(is_lower_101("C"))
    def test_is_lower_101_3(self):
        self.assertTrue(is_lower_101("a"))
    def test_is_lower_101_4(self):
        self.assertFalse(is_lower_101("D"))
    
    def test_char_rot_13_1(self):
        self.assertEqual(char_rot_13("b"), "o")
    def test_char_rot_13_2(self):
        self.assertEqual(char_rot_13("Z"), "M")






if __name__ == '__main__':
   unittest.main()

