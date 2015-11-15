INSERT_SERVER = """
        INSERT INTO Servers(link_id, url, server_string)
        VALUES(?, ?, ?)
    """


class Servers:

    @classmethod
    def insert_server(cls, connection, link_id, url, server_string):
        cursor = connection.cursor()

        cursor.execute(INSERT_SERVER, (link_id, url, server_string))
