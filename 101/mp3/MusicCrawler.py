import os
import mutagen
from song import Song
import datetime
from playlist import Playlist


class MusicCrawler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def get_data(self):
        for root, dirs, files in os.walk(self.dir):
            for filename in files:
                path = os.path.join(root, filename)
                if filename.endswith(".ogg") or filename.endswith(".mp3"):
                    song = mutagen.File(path, easy=True)
                    self.data.append(
                        Song(song['title'][0],
                             song['artist'][0],
                             song['album'][0],
                             song['length'][0]))

    def generate_playlist(self, playname="", shuff=False, repp=True):
        new_playlist = Playlist(name=playname, shuffle=shuff, repeat=repp)
        for song in self.data:
            new_playlist.add_song(song)
        return new_playlist
