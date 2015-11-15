import re
import queue
import json


class Panda:

    def __init__(self, name, email, gender):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(email, str):
            raise TypeError
        if not isinstance(gender, str):
            raise TypeError
        self.__name = name
        self.__email = email
        self.__gender = gender

    def panda_name(self):
        return self.__name

    def panda_email(self):
        return self.__email

    def panda_gender(self):
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
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def __str__(self):
        return "Name: {} \nemail: {} \ngender: {}".format(self.__name,
                                                          self.__email,
                                                          self.__gender)

    def has_panda(self, panda):
        return panda in self.social_network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")

        self.social_network[panda] = []

    def are_friends(self, panda1, panda2):
        if panda1 not in self.social_network or\
          panda2 not in self.social_network:

        return (panda1 in self.social_network[panda2] and
                panda2 in self.social_network[panda1])

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("Pandas already friends")

        self.social_network[panda1].append(panda2)
        self.social_network[panda2].append(panda1)

    def friends_of_panda(self, panda):
        if panda not in self.social_network:
            raise Exception("Panda not in the social network")
        return self.social_network[panda]

    def panda_connections(self, panda):
        connections = {}

        q = []
        visited = set()

        q.append((0, panda))
        visited.add(panda)

        while len(q) != 0:
            panda_data = q.pop(0)
            current_level = panda_data[0]
            current_node = panda_data[1]

            connections[current_node] = current_level

            for neighbour in self.social_network[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((current_level + 1, neighbour))

        return connections

    def connection_level(self, panda1, panda2):
        panda_table = self.panda_connections(panda1)

        if panda2 not in panda_table:
            return -1

        return panda_table[panda2]
    # def connection_level(self, panda1, panda2):
    #     if self.friends_of_panda(panda2) == []:
    #         return False

    #     if self.are_friends(panda1, panda2):
    #         return 1

    #     q = queue.Queue()
    #     path = [panda1]
    #     q.put(path)
    #     visited = set([panda1])

    #     while not q.empty():
    #         path = q.get()
    #         last_panda = path[-1]
    #         if last_panda == panda2:
    #             return len(path)-1
    #         for panda in self.social_network[last_panda]:
    #             if panda not in visited:
    #                 visited.add(panda)
    #                 q.put(path + [panda])

    #     return -1

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    # def how_many_gender_in_network(self, level, panda, gender):
    #     if gender not in ["male", "female"]:
    #         raise Exception("Invalid gender.")
    #     if level < 1:
    #         raise Exception("Invalid level.")
    #     gender_friends = []
    #     for panda1 in self.social_network:
    #         if (self.connection_level(panda1, panda) == level and
    #            panda1.panda_gender() == gender):
    #                 gender_friends.append(panda1)
    #     return gender_friends
    def how_many_gender_in_network(self, level, panda1, gender):
        panda_table = self.panda_connections(panda1)
        counter = 0

        for panda in panda_table:
            p_level = panda_table[panda]
            if (p_level != 0 and
                p_level < level and
               panda.panda_gender == gender):
                    counter += 1

        return counter

    # def pandas_in_social_network(self):
    #     pandas = [panda for panda in self.social_network]
    #     return pandas

    # def social_network_save(self, members_file, friends_file):
    #     pandas = {}
    #     for panda in self.pandas_in_social_network():
    #         pandas[panda.panda_name()] = panda.__dict__
    #     with open(members_file, "w") as file:
    #         file.write(json.dumps(pandas))

    def __repr__(self):
        for_save = {}

        for panda in self.social_network:
            friends = [
                    repr(p_friends) for p_friend in self.social_network[panda]
                      ]
            for_save[repr(panda)] = friends

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.__repr__(), indent=True))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:



def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    ani = Panda("Ani", "ani@pandamail.com", "female")
    tony = Panda("Tony", "tony@pandamail.com", "female")
    bubi = Panda("Pacho", "plamen@pandamail.com", "male")
    stefan = Panda("Stefcho", "stefcho@pandamail.com", "male")

    for panda in [ivo, rado, tony, bubi, ani, stefan]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)
    network.make_friends(rado, ani)
    network.make_friends(ivo, bubi)
    network.make_friends(ani, tony)
    print(network.panda_connections(ivo))
    # print(ivo == ivo)
    # print(network.pandas_in_social_network())
    # print(network.how_many_gender_in_network(2, ivo, "female"))
    # print(network.are_friends(ivo, rado))
    # print(network)
    # print(network.__dict__)
    # print(network.friends_of_panda(ivo))
    # print(network.connection_level(ivo, rado) == 1)  # True
    # print(network.connection_level(ivo, bubi) == 2)  # True
    # print(network.connection_level(ivo, stefan))
    # print(network.are_connected(ivo, bubi))

    # network.how_many_gender_in_network(1, rado, "female") == 1 # True


if __name__ == '__main__':
    main()
