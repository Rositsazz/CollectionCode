print("hi")
# this is the thuth
number = int(arguments[len(arguments)-1])
print(number)
file = open(filename, "w")
numbers = [randint(1, 1000) for x in range(1, number)]
file.write(" ".join(str(numbers))


print(numbers)

