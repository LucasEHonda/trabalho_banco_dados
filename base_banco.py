import mysql.connector



class Conexao:
    def __init__(self) -> None:
        self.con = mysql.connector.connect(user='admin', password='admin123', host='localhost')

        self.mycursor = self.con.cursor()

        self.mycursor.execute("SHOW DATABASES")

        exists = False
        for x in self.mycursor:
            if ('db_escolaIdiomas' in list(x)):
                exists = True

        if not exists:
            self.mycursor.execute("CREATE DATABASE db_escolaIdiomas")
        self.mycursor.execute("USE db_escolaIdiomas")

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

class Professor:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Professor (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

# class Turma:
#     def __init__(self, conn) -> None:
#         query = """CREATE TABLE IF NOT EXISTS Turma (
#     pessoa int PRIMARY KEY,
#     foreign key (pessoa) references Pessoa(cpf)
#     );"""
#         self.mycursor = conn.mycursor
#         self.mycursor.execute(query)

conn = Conexao()
pessoa = Pessoa(conn)
pessoa = Professor(conn)



class EstruturaBase:
    def __init__(self) -> None:
        pass