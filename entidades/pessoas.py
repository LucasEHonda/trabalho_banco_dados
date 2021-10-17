
class Pessoa:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Pessoa (
    cpf int PRIMARY KEY,
    nome varchar(255)  NOT NULL,
    cidade varchar(255)  NOT NULL,
    estado varchar(255)  NOT NULL
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)