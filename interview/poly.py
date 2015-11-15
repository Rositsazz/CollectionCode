class University:
    def __init__(self, name):
        self.courses = {}
        self.__name = name

    def __str__(self):
        return "{} University".format(self.__name)

    def has_course(self, course):
        return course in self.courses

    def add_course(self, course):
        if(course not in self.courses):
            self.courses[course] = course.grade


class Course:
    def __init__(self, course_name, grade):
        self.__course_name = course_name
        self.grade = grade

    def get_name(self):
        return self.__course_name

    def __str__(self):
        return "Course: {}, Grade: {} ".format(self.get_name(), self.grade)

    def __repr__(self):
        return "Course: {}, Grade: {} ".format(self.get_name(), self.grade)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.__str__())


Tehnicheski = University("Tehnicheski")
math = Course("Math", 5)
sport = Course("Sport", 6)
music = Course("Music", 4.7)
print(music)
geography = Course("Geography", 5.3)
Tehnicheski.add_course(math)
Tehnicheski.add_course(music)
Tehnicheski.add_course(geography)
Tehnicheski.add_course(sport)
for course in Tehnicheski.courses:
    print(course)

print(Tehnicheski.has_course(math))

print(Tehnicheski)
