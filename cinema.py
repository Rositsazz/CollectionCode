def free_seats_in_cinema(cinema):
    zero = 0
    j = 1
    free_seats = []
    for i in range(1, len(cinema) + 1):
        for element in cinema[i-1]:
            if element == zero:
                free_seats.append((i, j))
            j += 1
        j = 1

    return free_seats


def element_index(cinema):
    counter = len(cinema[0]) + 1
    index = None

    for i in range(len(cinema)):
        zeros = cinema[i].count(0)
        if zeros < counter and zeros != 0:
            index = i
            counter = cinema[i].count(0)

    return index


def order_of_seats(cinema):
    all_seats = len(cinema)*len(cinema[0])
    counter = 0
    zero = 0
    for row in cinema:
        for element in row:
            if element == zero:
                counter += 1

    if counter == all_seats:
        return free_seats_in_cinema(cinema)

    free_seats = []
    m = 0

    while m < len(cinema):
        index = element_index(cinema)
        for i in range(1, len(cinema) + 1):
            if i == index:
                for j in range(1, len(cinema[i - 1])):
                    if cinema[i][j] == 0:
                        free_seats.append((i + 1, j + 1))
                        cinema[i][j] = 1
        m += 1

    return free_seats


def main():
    # cinema = [[1, 1, 1],
    #           [1, 0, 0],
    #           [1, 0, 0],
    #           [1, 1, 0]]

    cinema = [[0, 0],
              [0, 0],
              [0, 0]]

    print(order_of_seats(cinema))


if __name__ == '__main__':
    main()
