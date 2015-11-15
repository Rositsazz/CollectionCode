class Song:

    def __init__(self, title="-", artist="-", album="-", length="-"):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def get_length(self):
        return self.length

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def __str__(self):
        return "{} - {} from {} - {}".format(
                                        self.artist,
                                        self.title,
                                        self.album,
                                        self.length)

    # def __eq__(self, other):
    #     return str(self) == str(other)

    def __repr__(self):
        return self.__str__()

    # def prepare_json(self):
    #     return self.__dict__

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__str__())

    def reverse_length_to_seconds(self):
        sec = self.get_length().split(":")
        if len(sec) == 3:
            return int(sec[0])*3600 + int(sec[1])*60 + int(sec[2])

        return int(sec[0])*60 + int(sec[1])

    def reverse_length_to_minutes(self):
        minutes = self.get_length().split(":")
        if len(minutes) == 3:
            return int(minutes[0])*60 + int(minutes[1])

        return int(minutes[0])

    def reverse_length_to_hours(self):
        hours = self.get_length().split(":")
        if len(hours) < 3:
            return 0
        return int(hours[0])

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.reverse_length_to_seconds()
        if minutes:
            return self.reverse_length_to_minutes()
        if hours:
            return self.reverse_length_to_hours()
        return self.get_length()

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}
