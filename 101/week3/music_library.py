class Song:

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_album(self):
        return self.__album

    def reverse_length_to_seconds(self):
        sec = self.__length.split(":")
        if len(sec) > 2:
            return int(sec[0])*3600 + int(sec[1])*60 + int(sec[2])

        return int(sec[0])*60 + int(sec[1])

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds or hours:
            return self.reverse_length_to_seconds()
        if minutes:
            return self.__length

    def __str__(self):
        return "{} - {} from {} - {}".format(
                                        self.__artist,
                                        self.__title,
                                        self.__album,
                                        self.__length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.__str__())


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.music_library = {}

    def get_name(self):
        return self.__name

    def get_repeat(self):
        return self.__repeat

    def get_shuffle(self):
        return self.__shuffle

    def has_song(self, song):
        return song in self.music_library

    def add_song(self, song):
        if self.has_song(song):
            raise Exception("The song is already in the playlist")

        self.music_library[song.get_title()] = song

    def add_songs(self, songs):
        for song in songs:
            if self.has_song(song):
                raise Exception("The song is already in the playlist")
            else:
                self.music_library["song: "] = song

    def total_length(self):
        return len(self.music_library)


def main():
    s = Song(title="Odin", artist="Manowar",
             album="The Sons of Odin", length="3:44")
    p = Song(title="Bring me to Life", artist="Evenescence",
             album="Fallen", length="4:12")
    code_songs = Playlist(name="Playlist")
    for song in [p, s]:
        code_songs.add_song(song)
    print(code_songs.__dict__)
    print(code_songs.total_length())
    # code_songs.add_songs([s, p])
    # print(code_songs.__dict__)
    # print(s)
    # print(p)
    # print(p.get_length())
    # print(s.length())
    # print(p.length(seconds=True))
    # print(p.length(hours=True))


if __name__ == '__main__':
    main()
