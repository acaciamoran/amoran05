import unittest
import conditional

class TestCases(unittest.TestCase):

    def test_cases_max_101_1(self):
        self.assertEqual(conditional.max_101(3,2),3)
    def test_cases_max_101_2(self):
        self.assertEqual(conditional.max_101(2,3),3)
   
    def test_cases_max_of_three_1(self):
        self.assertEqual(conditional.max_of_three(3,2,1),3)
    def test_cases_max_of_three_2(self):
        self.assertEqual(conditional.max_of_three(2,44,1),44)
    def test_cases_max_of_three_3(self):
        self.assertEqual(conditional.max_of_three(2,1,51),51)
   
    def test_cases_rental_late_fee_1(self):
        self.assertEqual(conditional.rental_late_fee(-1),0)
    def test_cases_rental_late_fee_3(self):
        self.assertEqual(conditional.rental_late_fee(8),5)
    def test_cases_rental_late_fee_4(self):
        self.assertEqual(conditional.rental_late_fee(11),7)
    def test_cases_rental_late_fee_5(self):
        self.assertEqual(conditional.rental_late_fee(24),19)
    def test_cases_rental_late_fee_6(self):
        self.assertEqual(conditional.rental_late_fee(28),100)


if __name__ == '__main__':
   unittest.main()
