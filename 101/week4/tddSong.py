import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odin", length="3:44")
        self.song2 = Song(title="Bring me to Life", artist="Evenescence",
                          album="Fallen", length="4:12")

    def test_exisiting_class_song(self):
        self.assertTrue(isinstance(self.song1, Song))

    def test_str_of_a_song(self):
        self.assertEqual(str(self.song1),
                         "Manowar - Odin from The Sons of Odin - 3:44")

    def test_if_two_songs_are_the_same(self):
        self.assertFalse(self.song1 == self.song2)

    def test_song_length_in_hours(self):
        self.assertTrue(self.song1.length(hours=True) == 0)

    def test_song_length_in_minutes(self):
        self.assertTrue(self.song1.length(minutes=True) == 3)

    def test_song_length_in_seconds(self):
        self.assertTrue(self.song1.length(seconds=True) == 224)

    def test_song_length(self):
        self.assertTrue(self.song1.length() == '3:44')

if __name__ == '__main__':
    unittest.main()
