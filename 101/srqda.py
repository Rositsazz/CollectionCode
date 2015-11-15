def sum_of_digits(n):
    return sum(to_digits(n))

#a = "123"
#print([x for x in a])

def to_digits(n):
    return [int(x) for x in str(n)]

def factorial(n):
    res = 1
    for x in range(1,n+1):
        res *= x
    return res

#145 = 1! +4! + 5!
def factorial_digits(n):
    return sum(factorial(x) for x in to_digits(n))

def palindrome(obj):
    return str(obj)[::-1]==str(obj)

#print(palindrome("123454321"))

def count_digits(n):
    return sum([1 for x in to_digits(n)])
    #sum==len(n) in this case


def to_number(digits):
    res = 0
    for digit in digits:
        digits_count = count_digits(digit)
        res  = res*(10**digits_count) +digits
    return res

#def fibonacci(n):

#def fibonacci_number(n):
    #return to_number(fibonacci(n))

def char_histogram(string):

    result = {}

    for element in string:
        if element in result :
            result[element]+=1
        else:
            result[element]=1

    return result

def char_histogram2(string):
    res = {}
#"aaaaAAAA".count("a")
# 4
#[x+1 for x in [1,2,3,4]]
# [2,3,4,5]
#{key: len(key) for key in ["Pyhton", "Django"]}

#{key: a.count(key) for key in a }


    return res

def p_score(n):
    if palindrome(n):
        return 1
    else:
        s = n + int(str(n)[::-1])
        return 1 + p_score(s)

print(p_score(48))



#[1,1,2,3,5,8,13]
#123*10 +138 = 123 + 13 = 136
#12313

def even(n):
    return n%2==0

def odd(n):
    return not even(n)

def is_hack(n):
    binaty_n = bin(n)[2:]
    is_palindrome = palindrome(binaty_n)
    has_odd_numbers = odd(binaty_n.count("1"))

    return is_palindrome and has_odd_numbers

def next_hack(n):
    n += 1
    while not is_hack(n):
        n += 1

    return n
