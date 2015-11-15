import requests


class Node:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return "{}".format(self.get_name())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.__str__())


class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def has_node(self, node):
        return node in self.graph

    def add_node(self, node):
        if self.has_node(node):
            raise Exception("Node Already in the Graph")

        self.graph[node] = []

    def exist_edge(self, node_a, node_b):
        return node_b in self.graph[node_a]

    def add_edge(self, node_a, node_b):
        if not self.has_node(node_a):
            self.add_node(node_a)

        if not self.has_node(node_b):
            self.add_node(node_b)

        if self.exist_edge(node_a, node_b):
            raise Exception("Already existing edge between nodes")

        self.graph[node_a].append(node_b)

    def get_graph(self):
        return self.graph

    def get_neighbors_for(self, node):
        if not self.has_node(node):
            self.add_node(node)

        return self.graph[node]

    def pprint(self):
        for user in self.graoh:
            print (user, self.graph[user])

    def find_path_between(self, node_a, node_b, path=[]):
        path = path + [node_a]
        if node_a == node_b:
            return [path]
        if not self.has_node(node_a):
            return []
        paths = []
        for node in self.graph[node_a]:
            if node not in path:
                newpaths = self.find_path_between(node,
                                                  node_b, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def path_between(self, node_a, node_b):
        return self.find_path_between(node_a, node_b) != []


class GitSocial:

    def __init__(self, username, level):
        self.username = username
        self.level = level
        self.graph = DirectedGraph()
        self.client_id = "b6063ab473f707db2576"
        self.client_secret = "b9fe272f8aec4188bdb22a8cb9b99dc390d630d6"
        self.domain_resouse = "https://api.github.com/users/"

    def get_info(self, user):
        url = self.domain_resouse + user + "/following?client_id=" + self.client_id + "&client_secret=" + self.client_secret
        following_json = requests.get(url).json()
        result = []
        for item in following_json:
            result.append(item["login"])

        return result

    def build_graph(self):
        visited = set()
        q = []
        levels_to_me = {}

        q.append(self.username)
        visited.add(self.username)
        levels_to_me[self.username] = 0

        while len(q) > 0:
            current_user = q.pop()

            if levels_to_me[current_user] > self.level:
                break

            for neighbour in self.get_info(current_user):
                self.graph.add_edge(current_user, neighbour)
                if neighbour not in visited:
                    levels_to_me[neighbour] = levels_to_me[current_user] + 1
                    visited.add(neighbour)
                    q.append(neighbour)

    def do_you_follow(self, user):
        return user in self.graph.get_neighbours_for(self.username)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.username, user)

    def does_he_she_follows(self, user):
        return self.username in self.graph.get_neighbours_for(user)

    def does_he_she_follows_indirectly(self, user):
        return self.graph.path_between(user, self.username)

    def who_follows_you_back(self):
        res = []
        q = []
        visited = set()

        q.append(self.name)
        visited.add(self.name)

        while not len(q) < 0:
            current_node = q.pop(0)
            if self.does_he_she_follows(current_node):
                res.append(current_node)

            for neighbour in self.graph.get_neighbours_for(current_node):
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
        return res
