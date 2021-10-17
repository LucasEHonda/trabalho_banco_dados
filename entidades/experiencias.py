
class Experiencia:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Experiencia (
    nome varchar(255) PRIMARY KEY
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class ExperienciaAtendeModalidade:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS ExperienciaAtendeModalidade (
    modalidade varchar(255) NOT NULL,
    foreign key (modalidade) references Modalidade(nome),
    experiencia varchar(255) NOT NULL,
    foreign key (experiencia) references Experiencia(nome)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)