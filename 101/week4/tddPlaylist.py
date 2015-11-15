import unittest
from song import Song
from playlist import Playlist


class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odin", length="3:44")
        self.song2 = Song(title="Bring me to Life", artist="Evenescence",
                          album="Fallen", length="4:12")
        self.playlist = Playlist(name="Code")

    def test_if_song_is_in_playlist(self):
        self.playlist.add_song(self.song1)
        self.assertTrue(self.playlist.has_song(self.song1))

if __name__ == '__main__':
    unittest.main()
