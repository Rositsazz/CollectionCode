import sqlite3
import uuid
import hashlib
import string
import getpass


from Client import Client
from settings import DB_NAME, SQL_FILE

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

INSERT_SQL = """INSERT INTO clients (username, password)
                VALUES (?, ?)"""

SELECT_QUERY = """SELECT id, username, balance, message
                  FROM clients
                  WHERE username = ? AND password = ? LIMIT 1"""

UPDATE_SQL_FOR_PASS = """UPDATE clients
                         SET password = ?
                         WHERE id = ? """

UPDATE_SQL_FOR_MESSAGE = """UPDATE clients
                            SET message = ?
                            WHERE id = ?"""

SELECT_PASSWORD_BY_USERNAME = """SELECT password
                                 FROM clients
                                 WHERE username = ?"""


def create_clients_table():

    with open(SQL_FILE, "r") as f:
        conn.executescript(f.read())
        conn.commit()


def change_message(new_message, logged_user):

    cursor.execute(UPDATE_SQL_FOR_MESSAGE, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):

    cursor.execute(UPDATE_SQL_FOR_PASS, (new_pass, logged_user.get_id()))
    conn.commit()


def hash_password(password):
    # uuid is used to generate a random number
    random_number = uuid.uuid4().hex
    hashable_pass = (hashlib.sha256(random_number.encode() +
                     password.encode()).hexdigest() + ':' + random_number)
    return hashable_pass


def register(username, password):
    password = password.strip()
    while validate_password(password) != []:
        password = getpass.getpass(stream=None)
    password = hash_password(password)
    cursor.execute(INSERT_SQL, (username, password))
    conn.commit()


def validate_password(password):
    errors = []
    if not any(x.isupper() for x in password):
        upper_error = "Enter at least one capital letter!"
        errors.append(upper_error)
        print(upper_error)

    if not any(x.islower() for x in password):
        lower_error = "Enter at least one lower letter!"
        errors.append(lower_error)
        print(lower_error)

    if len(password) < 8:
        len_error = "Enter password with more than 7 letters!"
        errors.append(len_error)
        print(len_error)

    if not any(x.isdigit() for x in password):
        digit_error = "Enter at least one digit!"
        errors.append(digit_error)
        print(digit_error)

    count = 0
    for x in password:
        if x in string.punctuation:
            count += 1
    if count == 0:
        special_symbol_error = "Enter at least one special symbol"
        errors.append(special_symbol_error)
        print(special_symbol_error)

    return errors


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def login(username, password):
    cursor.execute(SELECT_PASSWORD_BY_USERNAME, (username, ))
    hash_password = cursor.fetchone()[0]
    if check_password(hash_password, password):
        password = hash_password
        cursor.execute(SELECT_QUERY, (username, password))
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
