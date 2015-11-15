import sqlite3
import requests
import json


connection = sqlite3.connect("hackers.db")
cursor = connection.cursor()

""" course_name -> id"""
course_name_to_id = {}


def create_student(conn, cursor, student):
    insert_student = """
        INSERT INTO Students(name, github)
        VALUES(?, ?)
    """
    name = student["name"]
    github = student["github"]
    cursor.execute(insert_student, (name, github))
    conn.commit()

    return cursor.lastrowid


def create_course(connection, cursor, course):
    insert_course = """
        INSERT INTO Courses(name)
        VALUES(?)
    """
    course_name = course["name"]
    cursor.execute(insert_course, (course_name, ))
    connection.commit()

    return cursor.lastrowid


def create_relation(connection, cursor, student_id, course_id):
    insert_student_to_course = """
        INSERT INTO Students_to_Courses(student_id, course_id)
        VALUES(?, ?)
    """

    cursor.execute(insert_student_to_course, (student_id, course_id))
    connection.commit()


with open("hack_api.json", "r+") as f:
    info = json.load(f)

    for hacker in info:
        hacker_id = create_student(connection, cursor, hacker)
        courses = hacker["courses"]

        for course in courses:
            course_name = course["name"]
            if course_name in course_name_to_id:
                course_id = course_name_to_id[course_name]
            else:
                course_id = create_course(connection, cursor, course)
                course_name_to_id[course_name] = course_id

            create_relation(connection, cursor, hacker_id, course_id)
