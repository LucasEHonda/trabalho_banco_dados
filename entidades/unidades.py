
class Unidade:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Unidade (
    nome varchar(255) PRIMARY KEY,
    professor int NOT NULL,
    foreign key (professor) references Professor(pessoa)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)