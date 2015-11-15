# dunder == double under score - constructor
# class & instantion


class Panda:

    def __init__(self, name):
        print(self)
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


ivo = Panda("Ivo")
# print(ivo)
# rado = Panda("Rado")
# ivo.name = "Ivo Ivo"
# ivo.eat(2)
# print(ivo.weight)
print(type(ivo))
