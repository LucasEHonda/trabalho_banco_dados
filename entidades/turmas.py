
class Turma:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Turma (
    codigo varchar(255) PRIMARY KEY,
    professor int NOT NULL,
    foreign key (professor) references Professor(pessoa)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)


class TurmaPossuiLivro:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS TurmaPossuiLivro (
    livro varchar(255),
    foreign key (livro) references Livro(nome),
    turma varchar(255),
    foreign key (turma) references Turma(codigo)    
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)   