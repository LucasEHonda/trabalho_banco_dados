
class Horario:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Horario (
    codigo int PRIMARY KEY
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)