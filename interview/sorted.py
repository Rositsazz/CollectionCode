string = input("Enter string: ")
number = input("Enter number: ")


def string_permutations(string, number):
    number = int(number)
    counter = 0
    if(number <= 1 or number >= 100):
        return "Try again with number between (1, 100)"

    i = 0
    while(i < number):
        word = input("Enter another string: ")
        if(len(word) <= 100):
            if(sorted(string) == sorted(word)):
                counter += 1
        i += 1
    return counter

print(string_permutations(string, number))
