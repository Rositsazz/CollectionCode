import json
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

courses = []

with open("hack_api.json", "r+") as f:
    info = json.load(f)
    res = []
    for student in info:
        name = student["name"]
        github = student["github"]
        st_courses = student["courses"]
        # print(st_courses)
        cursor.execute("""INSERT INTO Students(name, github)
                          VALUES(?, ?)
                          """, (name, github))
        for course in st_courses:
            course_name = course["name"]
            if course_name not in courses:
                courses.append(course_name)
                cursor.execute("""INSERT INTO Courses(name)
                                  VALUES(?)""", (course_name,))

    # for student in info:
    #     st_courses = student["courses"]
    #     for course in st_courses:
    #         if course["name"] in courses:
    #             cursor.execute("""INSERT INTO Student_To_Course(student_id, course_id)
    #                               SELECT id, course_id
    #                               FROM Student_To_Course
    #                               JOIN Students
    #                               ON Student_To_Course.student_id = Students.id
    #                               JOIN Courses
    #                               ON Student_To_Course.student_id = Courses.course_id""")
connection.commit()
