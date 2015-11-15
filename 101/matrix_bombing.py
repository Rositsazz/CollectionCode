from copy import deepcopy


def sum_matrix(m):
    return sum([sum(row) for row in m])


def index_element(m):
    indexes = [(i, j) for i in range(len(m)) for j in range(len(m[0]))]
    return indexes


def find_neighbours(m, position):
    matrix = deepcopy(m)
    neighbours = []
    positions = index_element(matrix)
    a = (position[0]-1, position[1]-1)
    b = (position[0]-1, position[1])
    c = (position[0]-1, position[1]+1)
    d = (position[0], position[1]-1)
    e = (position[0], position[1]+1)
    f = (position[0]+1, position[1]-1)
    g = (position[0]+1, position[1])
    h = (position[0]+1, position[1]+1)

    if a in positions:
        neighbours += [matrix[position[0]-1][position[1]-1]]

    if b in positions:
        neighbours += [m[position[0]-1][position[1]]]

    if c in positions:
        neighbours += [matrix[position[0]-1][position[1]+1]]

    if d in positions:
        neighbours += [matrix[position[0]][position[1]-1]]

    if e in positions:
        neighbours += [matrix[position[0]][position[1]+1]]

    if f in positions:
        neighbours += [matrix[position[0]+1][position[1]-1]]

    if g in positions:
        neighbours += [matrix[position[0]+1][position[1]]]

    if h in positions:
        neighbours += [matrix[position[0]+1][position[1]+1]]

    return neighbours


def kraina_sum(m, bomb):
    matrix = deepcopy(m)
    kraina_suma = sum_matrix(matrix)
    element = matrix[bomb[0]][bomb[1]]
    for neighbour in find_neighbours(matrix, bomb):
        if neighbour < element:
            kraina_suma -= neighbour
        else:
            kraina_suma -= element
    return kraina_suma


def matrix_bombing_plan(m):
    matrix = deepcopy(m)
    result = {(i, j): 0 for i in range(len(matrix)) for j in range(len(matrix[0]))}
    positions = index_element(matrix)
    for key in positions:
        result[key] = kraina_sum(matrix, key)

    return result

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
