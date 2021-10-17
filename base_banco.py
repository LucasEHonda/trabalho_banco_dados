import mysql.connector



class Conexao:
    def __init__(self) -> None:
        self.NOME_BANCO = 'db_escolaIdiomas'
        self.con = mysql.connector.connect(user='admin', password='admin123', host='localhost')

        self.mycursor = self.con.cursor()

        self.mycursor.execute("SHOW DATABASES")

        exists = False
        for x in self.mycursor:
            if (self.NOME_BANCO in list(x)):
                exists = True

        if not exists:
            self.mycursor.execute("CREATE DATABASE db_escolaIdiomas")
        self.mycursor.execute("USE db_escolaIdiomas")
    
    def drop_banco(self) -> None:        
        self.mycursor.execute("DROP DATABASE db_escolaIdiomas")

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
    foreign key (pessoa) references Pessoa(cpf),
    codigo varchar (255) NOT NULL
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class Turma:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Turma (
    codigo varchar(255) PRIMARY KEY,
    professor int NOT NULL,
    foreign key (professor) references Professor(pessoa)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class Responsavel:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Responsavel (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class Aluno:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Aluno (
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

class Livro:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Livro (
    nome varchar(255) PRIMARY KEY
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


class Horario:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Horario (
    codigo int PRIMARY KEY
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class Unidade:
    def __init__(self, conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Unidade (
    nome varchar(255) PRIMARY KEY,
    professor int NOT NULL,
    foreign key (professor) references Professor(pessoa)
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

class Modalidade:
    def __init__(self,conn) -> None:
        query = """CREATE TABLE IF NOT EXISTS Modalidade (
    nome varchar(255) PRIMARY KEY
    );"""
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

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


class EstruturaBase:
    def __init__(self) -> None:
        self.conn = Conexao()
        self.pessoa = Pessoa(self.conn)
        self.professor = Professor(self.conn)
        self.turma = Turma(self.conn)
        self.experiencia = Experiencia(self.conn)
        self.modalidade = Modalidade(self.conn)
        self.responsavel = Responsavel(self.conn)
        self.experiencia_atende_modalidade = ExperienciaAtendeModalidade(self.conn)
        self.horario = Horario(self.conn)
        self.unidade = Unidade(self.conn)
        self.aluno = Aluno(self.conn)
        self.Responsavel_porAluno = ResponsavelPorAluno(self.conn)
        self.livro = Livro(self.conn)
        self.turma_possui_livro = TurmaPossuiLivro(self.conn)

banco = EstruturaBase()