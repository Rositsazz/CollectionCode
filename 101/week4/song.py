class Song:

    def __init__(self, title="-", artist="-", album="-", length="-"):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def get_length(self):
        return self.__length

    def get_title(self):
        return self.__title

    def __str__(self):
        return "{} - {} from {} - {}".format(
                                        self.__artist,
                                        self.__title,
                                        self.__album,
                                        self.__length)

    def __eq__(self, other):
        return str(self) == str(other)

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
