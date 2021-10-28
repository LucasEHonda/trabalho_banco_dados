class Procedures:
    def __init__(self, conn) -> None:
        self.mycursor = conn.mycursor
        self.pegar_alunos_por_turma()

    def pegar_alunos_por_turma(self):
        query = """CREATE PROCEDURE pegar_alunos_por_turma (cpf int) BEGIN
SELECT *
FROM Aluno
INNER JOIN Pessoa ON Aluno.pessoa = Pessoa.cpf
INNER JOIN Turma ON Aluno.pessoa = Turma.aluno
WHERE Turma.aluno = cpf; END
"""
        # try:
        #     self.mycursor.execute(query)
        # except Exception as e:
        #     print(e)
