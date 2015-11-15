import unittest
from social import PandaSocialNetwork
from pandas import Panda


class SocialTest(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.ivo = Panda("Ivo", "ivo@abv.bg", "male")
        self.rado = Panda("Rado", "rado@abv.bg", "male")

    def test_is_network_valid(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_is_panda_added_in_network(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.network.has_panda(self.ivo))

    def test_if_pandas_already_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_friends(self.ivo, self.rado))

    def test_if_panda_has_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.friends_of(self.ivo), self.rado)

    def test_connection_level_between_pandas(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.connection_level(self.ivo, self.rado), 1)

    def test_if_two_pandas_are_connected(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_connected(self.ivo, self.rado))

    def test_how_many_genders_in_panda_level_of_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(
            self.network.how_many_gender_in_network(1, self.ivo, "male"), 1)


if __name__ == '__main__':
    unittest.main()
