import queue


def connection_level(self, panda1, panda2):
    q = [[panda1]]
    visited = set()
    print(visited)

    while q:
        path = q.pop(0)
        last_panda = path[-1]

        if last_panda == panda2:
            return path

        elif last_panda not in visited:
            for current_neighbour in self.get(last_panda, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(last_panda)

    return -1

    #     def __str__(self):
    #     return "Name: {} \nemail: {} \ngender: {}".format(self.__name,
    #                                                       self.__email,
    #                                                       self.__gender)
    # # def connection_level(self, panda1, panda2):
    #     if (panda1 or panda2) not in self.social_network:
    #         return False

    #     if self.are_friends(panda1, panda2):
    #         return 1

    #     q = queue.Queue()
    #     path = [panda1]
    #     print(path)
    #     q.put(path)
    #     visited = set([panda1])
    #     print(visited)

    #     while not q.empty():
    #         path = q.get()
    #         print(path)
    #         last_panda = path[len(path)-1]
    #         if last_panda == panda2:
    #             return len(path)-1
    #         for panda in self[last_panda]:
    #             if panda not in visited:
    #                 visited.add(panda)
    #                 q.put(path + [panda])

    #     return -1

pandas = {'A': ['Bbb', 'C'],
          'Bbb': ['A', 'Ddd', 'E'],
          'C': ['A', 'F'],
          'Ddd': ['Bbb'],
          'E': ['Bbb', 'F'],
          'F': ['C', 'E'],
          'H': []}

print(connection_level(pandas, 'A', 'Ddd'))
# print(are_connected(pandas, 'A', 'B'))


def __panda_connections(self, panda):
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

        for neighbour in self.social_network[panda]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append((current_level + 1, neighbour))

    return connections
