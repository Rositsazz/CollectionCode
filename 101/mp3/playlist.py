import random
from song import Song
import datetime
from tabulate import tabulate
import json
import time


class Playlist:

    def __init__(self, name="-", repeat="NONE", shuffle=False):
        self.__songs = []
        self.__name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__shuffle_played_songs = set()
        self.__current_song_index = 0

    def get_name(self):
        return self.__name

    def has_song(self, song):
        return song in self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, song):
        try:
            self.__songs.remove(song)
        except ValueError:
            pass

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total_seconds = sum([song.get_length(seconds=True)
                            for song in self.__songs])
        return str(datetime.timedelta(seconds=total_seconds))

    def artists(self):
        all_artists = [song.artist for song in self.__songs]
        return {name: all_artists.count(name) for name in all_artists}

    def __has_next_song(self):
        return self.__current_song_index < len(self.__songs)

    def __shuffle(self):
        song = random.choice(self.__songs)

        while song in self.__shuffle_played_songs:
            song = random.choice(self.__songs)

        self.__shuffle_played_songs.add_song(song)

        if len(self.__shuffle_played_songs) == len(self.__songs):
            self.__shuffle_played_songs == set()
        return song

    def next_song(self):
        if self.repeat == "SONG":
            return self.__songs[self.__current_song_index]

        if self.shuffle:
            return self.__shuffle()

        if not self.__has_next_song() and self.repeat == "NONE":
            raise Exception("End of playlist")

        if not self.__has_next_song() and self.repeat == "PLAYLIST":
            self.__current_song_index = 0

        song = self.__songs[self.__current_song_index]
        self.__current_song_index += 1

        return song

    def pprint_playlist(self):
        table = {
                "artist": [],
                "song": [],
                "length": [],
                "album": []
        }
        for song in self.__songs:
            table["artist"].append(song.artist)
            table["song"].append(song.get_title())
            table["length"].append(song.get_length())
            table["album"].append(song.get_album())
        print(tabulate(table, headers="keys"))

    def prepare_json(self):
        data = {
            "name": self.__name,
            "songs": [song.prepare_json() for song in self.__songs]
        }

        return data

    def save(self):
        filename = self.__name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=True))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"],
                            title=dict_song["title"],
                            album=dict_song["album"],
                            length=dict_song["length"])
                p.add_song(song)

            return p


def test_load():
    p = Playlist.load("Manowar-songs.json")
    try:
        while True:
            song = p.next_song()
            print(str(song))
            time.sleep(1)
    except Exception as e:
        print(e)


def test_save():

    s = Song(album="The Sons of Odin",
             title="Odin",
             artist="Manowar",
             length="3:44")
    s1 = Song(album="The Sonds of Odin",
              title="Sons of Odin",
              artist="Manowar",
              length="6:08")
    p = Playlist("Manowar songs", repeat="SONG")
    p.add_song(s)
    p.add_song(s1)
    p.add_song(Song(album="Fallen",
                    title="Bring Me To Life (radio edit)",
                    artist="Evanesence",
                    length="3:30"))

    p.pprint_playlist()

    p.save()

    # p.test_load()
