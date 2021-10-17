
class Professor:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Professor (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf),
    codigo varchar (255) NOT NULL
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)