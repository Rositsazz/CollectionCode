import sql_manager


from settings import DB_NAME, SQL_FILE


class LoggedUser:

    def __init__(self, username, password, message=""):
        self.username = username
        self.password = password
        self.message = message
