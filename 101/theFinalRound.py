import collections


def count_words(arr):
    res = {}
    for word in arr:
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1

    return res


def unique_words_count(arr):
    res = {}
    suma = 0
    for word in arr:
        if word not in res:
            res[word] = 1
            suma += res[word]
    return suma


def nan_expand(times):
    no = "Not a "
    Nan = "NaN"
    if times == 0:
        return 0
    else:
        return no*times + Nan


def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not")) == expanded:
        return expanded.count("Not")
    return False


def prime_factorization(n):
    number = n
    factors = []
    i = 2
    while i <= number:
        while (n % i == 0):
            factors.append(i)
            n /= i
        i += 1

    res = []
    counter = collections.Counter(factors)
    for key in counter:
        res += [(key, counter[key])]

    return res


def group1(arr):
    d = {x: arr.count(x) for x in arr}
    print(d)
    res = []
    for key in d:
        if key not in res:
            res += [[key]*d[key]]

    return res


def check(arr):
    number = arr[0]
    array = [number]
    for i in range(1, len(arr)):
        if arr[i] == number:
            array.append(arr[i])
        else:
            break
    return array


def group(arr):

    res = []
    while len(arr) != 0:
        array = check(arr)
        res += [array]
        arr = arr[len(array):]

    return res


def max_consecutive(items):
    res = group(items)
    max_length = len(res[0])
    for i in range(len(res)):
        if max_length < len(res[i]):
            max_length = len(res[i])

    return max_length


def groupby(func, seq):
    result = {}
    for item in seq:
        if func(item) not in result:
            result[func(item)] = [item]
        else:
            result[func(item)].append(item)

    return result

# print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))


def prepare_meal(number):
    digits = 0
    n = number
    if number % 3 != 0 and number % 5 != 0:
        return " "
    else:
        while n % 3 == 0:
            digits += 1
            n = n/3

    string = ""
    string += " ".join(["spam" for i in range(digits)])
    if number % 5 == 0 and string == "":
        return "eggs"
    else:
        string += " and eggs"

    return string


def reduce_file_path(path):
    result = "/"
    path = path.split("/")

    path_elements = []
    for item in path:
        if item != "." and item != "":
            path_elements.append(item)

    length = len(path_elements)
    folders = []
    for i in range(length - 1):
        if path_elements[i] != "..":
            if (i+1 <= length and path_elements[i+1] != ".."):
                folders.append(path_elements[i])

    if length != 0 and path_elements[length-1] != "..":
        folders.append(path_elements[length-1])
    result += "/".join(folders)
    return result


def is_an_bn(word):
    length = len(word)
    str1 = word[:length//2]
    str2 = word[length//2:]
    for char in str1:
        if char != "a":
            return False
    for char in str2:
        if char != "b":
            return False
    return True


def to_digits(number):
    return [int(x) for x in str(number)]


def is_credit_card_valid(number):
    digits = to_digits(number)

    sum_digits = sum([1 for x in digits])

    suma = 0
    if sum_digits % 2 != 0:
        for i in range(len(str(number))):
            if i % 2 == 0:
                suma += digits[i]
            else:
                suma += sum(to_digits(digits[i] * 2))

        return suma % 10 == 0


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


def goldbach(n):
    primes = [x for x in range(2, n+1) if is_prime(x)]
    results = []
    for number in primes:
        if number <= n / 2:
            results.append([(number, numb) for numb in primes if number + numb == n])

    return [res[0] for res in results if res != []]


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


def reduce_file_path1(path):
    result = []
    parts = [part for part in path.split("/") if part not in ["", "."]]

    print(parts)

    while len(parts) != 0:
        part = parts.pop()

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            result.insert(0, part)

    return "/" + "/".join(result)


def main():
    print(reduce_file_path1("/etc/../etc/../etc/../"))

if __name__ == '__main__':
    main()
