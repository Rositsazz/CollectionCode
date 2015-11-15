import copy


def is_prime(n):

    start = 2
    is_prime = True

    if n == 0:
        return False

    elif n == 1:
        return False

    elif n < 0:
        return False

    elif n > 1:
        while start < n:
            if n % start == 0:
                is_prime = False
                break
            start += 1
        return is_prime


def sum_of_divisors(n):
    sum_divisors = 0
    integer = 1
    middle = n//2

    if n == 0:
        return 0
    elif is_prime(n):
        return n+1
    else:
        while integer <= middle:
            if n % integer == 0:
                sum_divisors += integer
            integer += 1

        return sum_divisors+n


def sum_of_divisors2(n):
    return sum([x for x in range(1, n+1) if n % x == 0])


def prime_number_of_divisors(n):
    sum_divisors = []
    integer = 1
    middle = n//2

    if n == 0:
        lenght = len(sum_divisors)
        return is_prime(lenght)

    else:
        while integer <= middle:
            if n % integer == 0:
                sum_divisors += [integer]
            integer += 1

        lenght = len(sum_divisors) + 1

        return is_prime(lenght)


def contains_digit(number, digit):
    return str(digit) in str(number)


def contains_digits(number, digits):
    contains = True
    for digit in digits:
        if contains_digit(number,digit) == True:
            continue
        else:
            contains = False
    return contains


def is_number_balanced(n):
    digits = [int(x) for x in str(n)]
    middle = len(digits)//2

    sum1 = sum(digits[:middle])
    sum2 = 0
    if len(digits) % 2 == 0:
        sum2 = sum(digits[middle:])
    else:
        sum2 = sum(digits[(middle+1):])

    return sum1 == sum2


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    new_integer = [int(x) for x in str(n)]

    i = 0
    while i < len(new_integer)-1:
        if new_integer[i] == new_integer[i+1]:
            new_integer.insert(i+1, 0)
        elif (new_integer[i] + new_integer[i+1]) % 10 == 0:
            new_integer.insert(i+1, 0)
        i += 1

    new_number = 0
    for item in new_integer:
        new_number = new_number*10 + item

    return new_number


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def sum_matrix(m):
    return sum([sum(row) for row in m])


def index_element(m):
    indexes = []

    for i in range(len(m)):
        for j in range(len(m[0])):
            index_el = (i, j)
            indexes += [index_el]
    return indexes


def check_small(m, actual_position, position2):
    is_smaller = False
    if m[position2[0]][position2[1]] - m[actual_position[0]][actual_position[1]] >= 0:
        return True
    return is_smaller


def find_neighbours(m, position):
    neighbours = []
    positions = index_element(m)
    a = (position[0]-1, position[1]-1)
    b = (position[0]-1, position[1])
    c = (position[0]-1, position[1]+1)
    d = (position[0], position[1]-1)
    e = (position[0], position[1]+1)
    f = (position[0]+1, position[1]-1)
    g = (position[0]+1, position[1])
    h = (position[0]+1, position[1]+1)

    if a in positions:
        print()
        neighbours += [m[position[0]-1][position[1]-1]]

    if b in positions:
        neighbours += [m[position[0]-1][position[1]]]

    if c in positions:
        neighbours += [m[position[0]-1][position[1]+1]]

    if d in positions:
        neighbours += [m[position[0]][position[1]-1]]

    if e in positions:
        neighbours += [m[position[0]][position[1]+1]]

    if f in positions:
        neighbours += [m[position[0]+1][position[1]-1]]

    if g in positions:
        neighbours += [m[position[0]+1][position[1]]]

    if h in positions:
        neighbours += [m[position[0]+1][position[1]+1]]

    return neighbours


def div(m, act, position):
    if m[act[0]][act[1]] > m[position[0]][position[1]]:
        return 0
    else:
        return m[position[0]][position[1]] - m[act[0]][act[1]]


def reduce(m, position):
    for neighbour in find_neighbours(m, position):

        neighbour = div(m, position, neighbour)
        print(div(m, position, neighbour))
    return m


def matrix_bombing_plan(m):
    result = { (i, j):sum_matrix(m) for i in range(len(m)) for j in range(len(m[0]))}

    suma = sum_matrix(m)
    positions = index_element(m)
    for key in positions:

        result[key] = suma - sum(find_neighbours(m, key))
    return result
