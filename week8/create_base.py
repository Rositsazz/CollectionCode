import sqlite3


connection = sqlite3.connect("hackers.db")
cursor = connection.cursor()

create_students_table = """
CREATE TABLE IF NOT EXISTS Students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT
)
"""

cursor.execute(create_students_table)

create_courses_table = """
CREATE TABLE IF NOT EXISTS Courses(
    course_id INTEGER PRIMARY KEY,
    name TEXT
)
"""

cursor.execute(create_courses_table)

create_students_to_courses = """
CREATE TABLE IF NOT EXISTS Students_to_Courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
"""

cursor.execute(create_students_to_courses)

connection.commit()
