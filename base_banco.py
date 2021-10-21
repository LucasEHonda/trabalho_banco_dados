from conexao import Conexao
from entidades.alunos import Aluno
from entidades.experiencias import Experiencia, ExperienciaAtendeModalidade
from entidades.horarios import Horario
from entidades.livros import Livro
from entidades.modalidades import Modalidade
from entidades.pessoas import Pessoa
from entidades.professores import Professor
from entidades.responsaveis import Responsavel, ResponsavelPorAluno
from entidades.turmas import Turma, TurmaPossuiLivro
from entidades.unidades import Unidade


class EstruturaBase:
    def __init__(self) -> None:
        self.conn = Conexao()
        self.pessoa = Pessoa(self.conn)
        self.professor = Professor(self.conn)
        self.experiencia = Experiencia(self.conn)
        self.modalidade = Modalidade(self.conn)
        self.responsavel = Responsavel(self.conn)
        self.experiencia_atende_modalidade = ExperienciaAtendeModalidade(self.conn)
        self.horario = Horario(self.conn)
        self.unidade = Unidade(self.conn)
        self.aluno = Aluno(self.conn)
        self.responsavel_por_aluno = ResponsavelPorAluno(self.conn)
        self.livro = Livro(self.conn)
        self.turma = Turma(self.conn)
        self.turma_possui_livro = TurmaPossuiLivro(self.conn)

    def criar(self, entidade, dados):
        entidade.criar(dados)

    def deletar(self, entidade, dados):
        entidade.deletar(dados.get("coluna"), dados.get("valor"))

    def pegar(self, entidade, dados):
        resultados = entidade.pegar(dados.get("coluna"), dados.get("valor"))

        for resultado in resultados:
            print(resultado)


# banco = EstruturaBase()

# banco.criar(
#     banco.pessoa,
#     {
#         "cpf": int("054742"),
#         "aniversario": "07/12/1999",
#         "nome": "Lucas Honda",
#         "sexo": "Masculino",
#         "cidade": "Brasilia",
#         "estado": "DF",
#     },
# )
# banco.criar(banco.professor, {"pessoa": int("054742"), "codigo": "#001"})
# banco.criar(banco.aluno, {"pessoa": int("054742")})
# banco.criar(banco.unidade, {"professor": int("054742"), "nome": "brasilia - Asa sul"})
# banco.criar(banco.responsavel, {"pessoa": int("054742")})
# banco.criar(banco.horario, {"codigo": 235})
# banco.criar(banco.livro, {"nome": "como ser um cara legal"})
# banco.criar(banco.modalidade, {"nome": "presencial"})
# banco.criar(banco.experiencia, {"nome": "EAD"})
# banco.criar(
#     banco.turma,
#     {
#         "codigo": "#T01",
#         "professor": int("054742"),
#         "aluno": int("054742"),
#         "horario": 235,
#         "modalidade": "presencial",
#     },
# )
# banco.criar(
#     banco.experiencia_atende_modalidade,
#     {"modalidade": "presencial", "experiencia": "EAD"},
# )
# banco.criar(
#     banco.responsavel_por_aluno, {"aluno": int("054742"), "responsavel": int("054742")}
# )
# banco.criar(
#     banco.turma_possui_livro, {"livro": "como ser um cara legal", "turma": "#T01"}
# )

# banco.pegar(
#     banco.turma_possui_livro, {"coluna": "livro", "valor": "como ser um cara legal"}
# )

# banco.deletar(
#     banco.turma_possui_livro, {"coluna": "livro", "valor": "como ser um cara legal"}
# )


# banco.conn.drop_banco()
