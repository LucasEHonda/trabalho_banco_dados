
class Responsavel:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Responsavel (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class ResponsavelPorAluno:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS ResponsavelPorAluno (
    aluno int,
    foreign key (aluno) references Aluno(pessoa),
    responsavel int,
    foreign key (responsavel) references Responsavel(pessoa)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)    