def setify(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    return new_list


def second_largest(numbers):
    new_list = setify(numbers)
    new_list.sort()

    if len(new_list) < 2:
        return False

    return new_list[len(new_list) - 2]


def main():
    print(second_largest([100, 100, 90]))
    print(second_largest([5, 5]))
    print(second_largest([2, 1]))
    print(second_largest([]))
    print(second_largest([4, 3, 5, 4, 6, 7, 7, 7, 8]))

if __name__ == '__main__':
    main()
