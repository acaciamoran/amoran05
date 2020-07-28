import unittest
import convert


class TestCases(unittest.TestCase):

    def test_convert_1(self):
        string = '5'
        float_value = -1
        self.assertEqual(convert.float_default(string, float_value), 5)
    def test_convert_2(self):
        string = 'katie'
        float_value = -1
        self.assertEqual(convert.float_default(string, float_value), -1)

if __name__ == '__main__':
    unittest.main()

