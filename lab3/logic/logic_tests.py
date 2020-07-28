import unittest
import logic

class TestCases(unittest.TestCase):

    def test_case_is_even_1(self):
      self.assertTrue(logic.is_even(4))
    def test_case_is_even_2(self):
      self.assertFalse(logic.is_even(3))

    def test_case_is_an_interval_1(self):
        self.assertTrue(logic.is_an_interval(2))
    def test_case_is_an_interval_2(self):
        self.assertFalse(logic.is_an_interval(1))

    def test_case_is_an_interval_3(self):
        self.assertTrue(logic.is_an_interval(48))
    def test_case_is_an_interval_4(self):
        self.assertFalse(logic.is_an_interval(93))

    def test_case_is_an_interval_5(self):
        self.assertTrue(logic.is_an_interval(19))
    def test_case_is_an_interval_6(self):
        self.assertFalse(logic.is_an_interval(20))


    def test_case_is_an_interval_7(self):
        self.assertTrue(logic.is_an_interval(101))
    def test_case_is_an_interval_8(self):
        self.assertFalse(logic.is_an_interval(104))



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
