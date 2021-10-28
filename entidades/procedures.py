class Procedure:
    def __init__(self, conn) -> None:
        self.conn = conn
        self.mycursor = conn.mycursor
        self.verifica_existe_pessoa_cadastrada()

    def verifica_existe_pessoa_cadastrada(self):
        query = """CREATE PROCEDURE verifica_existe_pessoa_cadastrada (cpf INT)
  BEGIN
    SELECT *
    FROM   (SELECT Pessoa.nome, Aluno.pessoa
            FROM   Pessoa
                   INNER JOIN Aluno
                           ON Pessoa.cpf = Aluno.pessoa
                           WHERE  Aluno.pessoa = cpf
            UNION
            SELECT Pessoa.nome, Professor.pessoa
            FROM   Pessoa
                   INNER JOIN Professor
                           ON Pessoa.cpf = Professor.pessoa
                           WHERE  Professor.pessoa = cpf
            UNION
            SELECT Pessoa.nome, Responsavel.pessoa
            FROM   Pessoa
                   INNER JOIN Responsavel
                           ON Pessoa.cpf = Responsavel.pessoa
                           WHERE  Responsavel.pessoa = cpf) AS t
    WHERE  cpf = cpf;
  END 
"""
        try:
            self.mycursor.execute(query)
            self.conn.con.commit()
        except Exception as e:
            print(e)
