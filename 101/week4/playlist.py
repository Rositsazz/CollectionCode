from song import Song


class Playlist:

    def __init__(self, name="-", repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.music_library = {}

    def get_name(self):
        return self.__name

    def has_song(self, song):
        return song.get_title() in self.music_library

    def add_song(self, song):
        if self.has_song(song):
            raise Exception("The song is already in the playlist")

        self.music_library[song.get_title()] = song
