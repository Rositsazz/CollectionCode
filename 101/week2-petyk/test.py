# dunder == double under score - constructor
# class & instantion


class Panda:

    def __init__(self, name):
        # print(self)
        self.age = 0
        self.weight = 30
        self.name = name

    # mutating methods
    def grow_up(self):
        self.age += 1

    def eat(self, amount):
        self.weight += amount//2

    def sleep(self):
        self.weight += 1

    def __add__(self, other):
        return Panda(" ".join([self.name, other.name]))


class Person:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name


class Dog:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name

ivo = Panda("Ivo")
# print(ivo)
# rado = Panda("Rado")
# ivo.name = "Ivo Ivo"
# ivo.eat(2)
# print(ivo.weight)
print(type(ivo))


# def greet(thing):
#     print("Hello, {}".format(thing.say_name()))

hash("Panda") - > return hashable number

# dunder == double under score - constructor
# class & instantion


class Panda:

    def __init__(self, name):
        # print(self)
        self.age = 0
        self.weight = 30
        self.name = name

    # mutating methods
    def grow_up(self):
        self.age += 1

    def eat(self, amount):
        self.weight += amount//2

    def sleep(self):
        self.weight += 1

    def __add__(self, other):
        return Panda(" ".join([self.name, other.name]))

    def __str__(self):
        return "I am Panda {} and I am {} old".format(self.name, self. age)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name + str(self.weight))

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight

    def __int__(self):
        return self.weight


ivo = Panda("Ivo")
# print(type(ivo))
print(ivo)
