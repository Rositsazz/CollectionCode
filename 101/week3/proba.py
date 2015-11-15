import json


# neorientiran graf bez tegla
# spisyk na sysedite

graph = {
    "1": ["2", "3", "5"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9"],
    "11": ["12"],
    "12": ["11"],
}
# otgovarq dali ima pyt mejdu start i end


def bfs(graph, start, end):
    Q = []
    visited = set()
    Q.append(start)
    visited.add(start)

    while len(Q) != 0:
        current_node = Q.pop(0)

        if current_node == end:
            return True

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                Q.append(neighbour)

    return False


def bfs2(graph, start, end):
    Q = []
    visited = set()
    Q.append((0, start))
    visited.add(start)

    while len(Q) != 0:
        node_data = Q.pop(0)

        current_level = node_data[0]
        current_node = node_data[1]
        if current_node == end:
            return current_level

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                Q.append((current_level + 1, neighbour))

    return -1

# namirane na nai-kratkiq pyt


def bfs3(graph, start, end):
    Q = []
    visited = set()
    path_to = {}
    Q.append(start)
    visited.add(start)
    path = []

    path_to[start] = None
    found = False
    while len(Q) != 0:
        current_node = Q.pop(0)

        if current_node == end:
            found = True
            break

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                path_to[neighbour] = current_node
                visited.add(neighbour)
                Q.append(neighbour)

    if found:
        while end is not None:
            path.append(end)
            end = path_to[end]

    return path.reverse()


print(bfs(graph, "1", "9"))
print(bfs(graph, "1", "19"))
print(bfs2(graph, "1", "9"))
path_table = bfs3(graph, "1", "9")
print(json.dumps(path_table, indent=True))
