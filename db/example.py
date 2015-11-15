import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

create_movie_table = """CREATE TABLE IF NOT EXISTS MOVIE (
                         TITLE VARCHAR(255) NOT NULL,
                         YEAR INTEGER NOT NULL,
                         LENGTH INTEGER,
                         INCOLOR CHAR(1),
                         STUDIONAME CHAR(50),
                         PRODUCERC INTEGER
                        )"""
cursor.execute(create_movie_table)

create_moviestar_table = """CREATE TABLE IF NOT EXISTS MOVIESTAR (
 NAME CHAR(30) NOT NULL,
 ADDRESS VARCHAR(255),
 GENDER CHAR(1),
 BIRTHDATE DATETIME
)"""
cursor.execute(create_moviestar_table)

create_starin_table = """CREATE TABLE IF NOT EXISTS STARSIN (
    MOVIETITLE VARCHAR(255) NOT NULL,
    MOVIEYEAR INTEGER NOT NULL,
    STARNAME CHAR(30) NOT NULL
)"""
cursor.execute(create_starin_table)

create_movieexec_table = """CREATE TABLE IF NOT EXISTS MOVIEEXEC (
    CERT INTEGER NOT NULL,
    NAME CHAR(30),
    ADDRESS VARCHAR(255),
    NETWORTH INTEGER
)"""
cursor.execute(create_movieexec_table)

create_studio_table = """CREATE TABLE IF NOT EXISTS STUDIO (
    NAME CHAR(50) NOT NULL,
    ADDRESS VARCHAR(255),
    PRESC INTEGER
)"""
cursor.execute(create_studio_table)

connection.commit()


