import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_pounds_to_kg_1(self):
        self.assertAlmostEqual(funcs.pounds_to_kg(140), 63.50288 )
    def test_pounds_to_kg_2(self):
        self.assertAlmostEqual(funcs.pounds_to_kg(100), 45.3592)
    def test_get_mass_object_1(self):
        self.assertEqual(funcs.get_mass_object("t"), 0.1)
    def test_get_mass_object_2(self):
        self.assertEqual(funcs.get_mass_object("p"), 1.0)
    def test_get_mass_object_3(self):
        self.assertEqual(funcs.get_mass_object("r"), 3.0)
    def test_get_mas_object_4(self):
        self.assertEqual(funcs.get_mass_object("g"), 5.3)
    def test_get_mass_object_5(self):
        self.assertEqual(funcs.get_mass_object("l"), 9.07)
    def test_get_mass_object_6(self):
        self.assertEqual(funcs.get_mass_object("k"), 0.0)
    def test_get_velocity_object_1(self):
        self.assertEqual(funcs.get_velocity_object(10), 7.0)
    def test_get_velocity_object_2(self):
        self.assertEqual(funcs.get_velocity_object(40), 14.0)
    def test_get_velocity_skater_1(self):
        self.assertEqual(funcs.get_velocity_skater(5,2,10),4)
    def test_get_velocity_skater_2(self):
        self.assertEqual(funcs.get_velocity_skater(10,20,3),6)
if __name__ =="__main__":
    unittest.main()
