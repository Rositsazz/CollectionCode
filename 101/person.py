"""
CREATE TABLE People(
    person_id INTEGER PRIMARY KEY,
    person_name TEXT,
    person_age INTEGER
);


INSERT INTO People(person_name, person_age)
VALUES("Gosho", 17);
"""
import inspect


def map_class_to_table(cls):
    print(cls.__dict__)
    print(inspect.getmembers(cls))

class Person:
    name = ""
    age = 0
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


map_class_to_table(Person)
# gosho = Person("Gosho", 17)
# map_class_to_table(gosho)
