import re


class Panda:

    def __init__(self, name, email, gender):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(email, str):
            raise TypeError
        if gender not in ["male", "female"]:
            raise TypeError
        self.__name = name
        self.__email = email
        self.__gender = gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def __str__(self):
        return "I am Panda. My name is {}".format(self.__name)

    def __repr__(self):
        return "Panda: {}, {}, {} ".format(self.__name,
                                           self.__email,
                                           self.__gender)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.__str__())

    def valid_email(self):
        match = re.search(r'[^@|\s]+@[^@]+\.[^@|\s]+', self.__email)

        if match:
            return ("valid email: {}".format(match.group()))
        else:
            return ("not valid email")

    def isMale(self):
        return self.gender() == "male"

    def isFemale(self):
        return self.gender() == "female"
