class HashMap:

    def __init__(self):
        self.dict = {}

    def has(self, key):
        return key in self.dict

    def add(self, key, value):
        if key not in self.dict:
            self.dict[key] = value

    def get(self, key):
        return self.dict[key]

    def remove(self, key):
        self.dict.pop(key)

    def iterate(self):
        for key, value in self.dict.items():
            print("{} : {}".format(key, value))

a = HashMap()
a.add("elena", 108)
print(a.has("elena"))
print(a.get("elena"))
a.iterate()
print(a.remove("elena"))
