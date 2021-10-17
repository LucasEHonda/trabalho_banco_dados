class Livro:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Livro (
    nome varchar(255) PRIMARY KEY
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query) 