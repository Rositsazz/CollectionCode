import unittest
from pandas import Panda


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_exisiting_class_panda(self):
        self.assertTrue(isinstance(self.ivo, Panda))

    def test_is_name_str(self):
        with self.assertRaises(TypeError):
            Panda(10, "ivo@pandamail.com", "male")

    def test_is_panda_gender_valid(self):
        with self.assertRaises(TypeError):
            Panda("Ivo", "ivo@mail.bg", 10)

    def test_panda_has_name(self):
        self.assertTrue(self.ivo.name())

    def test_panda_has_email(self):
        self.assertTrue(self.ivo.name(), "Ivo")

    def test_equal_pandas(self):
        ivo = Panda("Ivo", "i@abv.bg", "male")
        ivo2 = Panda("Ivo", "i2@abv.bg", "male")
        self.assertFalse(ivo == ivo2)

    def test_is_panda_male(self):
        self.assertTrue(self.ivo.isMale())

    def test_is_panda_female(self):
        self.assertFalse(self.ivo.isFemale())


if __name__ == '__main__':
    unittest.main()
