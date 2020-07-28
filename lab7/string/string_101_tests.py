import unittest
from string_101 import *


class TestString(unittest.TestCase):

    def test_str_rot_13_1(self):
        string = "hello"
        newstring = "uryyb"
        self.assertEqual(str_rot_13(string), newstring)

    def test_str_rot_13_2(self):
        string = "Sentence"
        newstring = "Fragrapr"
        self.assertEqual(str_rot_13(string), newstring)
    
    def test_str_translate_1(self):
        string = "hello"
        newstring = "hesso"
        self.assertEqual(str_translate_101(string, "l", "s"), newstring)
    def test_str_translate_2(self):
        string = "Sentence"
        newstring = "Sxntxncx"
        self.assertEqual(str_translate_101(string, "e", "x"), newstring)




if __name__ == '__main__':
   unittest.main()

