
class Aluno:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Aluno (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)