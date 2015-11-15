import json


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def has_panda(self, panda):
        return panda in self.social_network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")

        self.social_network[panda] = []

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("Pandas are already friends")

        self.social_network[panda1].append(panda2)
        self.social_network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return (panda1 in self.social_network[panda2] and
                panda2 in self.social_network[panda1])

    def friends_of(self, panda):
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

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def how_many_gender_in_network(self, level, panda1, gender):
        panda_table = self.panda_connections(panda1)
        counter = 0

        for panda in panda_table:
            p_level = panda_table[panda]
            if (p_level != 0 and
                p_level <= level and
               panda.gender() == gender):
                    counter += 1

        return counter

    def data(self):
        for_save = {}

        for panda in self.social_network:
            friends = [
                    repr(p_friend) for p_friend in self.social_network[panda]
                      ]
            for_save[repr(panda)] = friends

        return for_save

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.data(), indent=4))
            f.close()

    # @staticmethod
    def load(self, filename):
        with open(filename, "r") as f:
            contents = f.read()
            filedata = json.loads(contents)
