def magic_square(square):
    sum_main_diagonal = sum([square[i][i] for i in range(len(square))])

    sec_diagonal = []
    i = 0
    j = len(square) - 1
    for row in square:
        sec_diagonal.append(square[i][j])
        i += 1
        j -= 1

    sum_sec_diagonal = sum(sec_diagonal)
    if sum_main_diagonal != sum_sec_diagonal:
        return False

    for i in range(len(square)):
        if sum_main_diagonal != sum(square[i]):
            return False

    sum_col = 0
    i = 0
    for row in square:
        sum_col += row[i]
        i += 1

    return sum_main_diagonal == sum_col


square1 = [[23, 28, 21], [22, 24, 26], [27, 20, 25]]
print(magic_square(square1))
