def factorial(n):
    if n == 0:
        return 1

    product = 1
    while n != 1:
        product *= n
        n -= 1

    return product


def fibonacci(n):

    if n == 0:
        return 1

    elif n == 1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)


def nth_fibonacci(n):

    lst = []
    n = n-1
    while n >= 0:
        lst += [fibonacci(n)]
        n -= 1

    lst.reverse()
    return lst


def sum_of_digits(n):

    sum_digits = 0
    while n != 0:
        sum_digits += (n % 10)
        n = n//10

    return sum_digits


def fact_digits(n):

    sum_digits = 0
    while n != 0:
        sum_digits += factorial(n % 10)
        n = n//10

    return sum_digits


def palindrome(obj):
    obj = str(obj)
    new_obj = obj[::-1]
    return obj == new_obj


def to_digits(n):

    digits = []

    while n > 0:

        digit = n % 10
        digits += [digit]
        n = n//10

    digits.reverse()

    return digits


def to_number(digits):
    number = ""
    for digit in digits:
        number += str(digit)

    return int(number)


def fib_number(n):
    return to_number(nth_fibonacci(n))


def count_vowels(string):
    vowels = "aueyioAUEYIO"
    counter = 0
    for char in string:
        if char in vowels:
            counter += 1

    return counter


def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    counter = 0
    for char in string:
        if char in consonants:
            counter += 1

    return counter


def char_histogram(string):

    result = {}

    for element in string:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1

    return result


def p_score(n):
    if palindrome(n):
        return 1
    else:
        s = n + int(str(n)[::-1])
        return 1 + p_score(s)


def is_increasing(seq):
    index = 0
    counter = 0
    while index < len(seq)-1:
        if seq[index] < seq[index+1]:
            counter += 1
        index += 1

    return counter == index


def is_decreasing(seq):
    index = 0
    counter = 0
    while index < len(seq)-1:
        if seq[index] > seq[index+1]:
            counter += 1
        index += 1

    return counter == index


def is_hack(number):
    number = bin(number)[2:]

    counter = 0
    for char in str(number):
        if char == "1":
            counter += 1
    if counter % 2 == 1:
        return palindrome(number)


def next_hack(n):
    number = n + 1
    while True:
        if is_hack(number):
            return number
        number += 1
