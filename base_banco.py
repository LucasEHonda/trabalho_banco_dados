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
from entidades.procedures import Procedures


class EstruturaBase:

    conn = Conexao()
    pessoa = Pessoa(conn)
    professor = Professor(conn)
    experiencia = Experiencia(conn)
    modalidade = Modalidade(conn)
    experiencia_atende_modalidade = ExperienciaAtendeModalidade(conn)
    horario = Horario(conn)
    unidade = Unidade(conn)
    livro = Livro(conn)
    turma = Turma(conn)
    aluno = Aluno(conn)
    responsavel = Responsavel(conn)
    responsavel_por_aluno = ResponsavelPorAluno(conn)
    turma_possui_livro = TurmaPossuiLivro(conn)

    def __init__(self) -> None:
        Procedures(self.conn)
        self.script()

    def criar(self, entidade, dados):
        entidade.criar(dados)

    def deletar(self, entidade, dados):
        entidade.deletar(dados.get("coluna"), dados.get("valor"))

    def pegar(self, entidade, dados=None, tudo=False):
        resultados = entidade.pegar(dados.get("coluna"), dados.get("valor")) if dados else entidade.pegar(tudo=tudo)
        return [resultado for resultado in resultados]
    
    def pegar_outra_tabela(self, entidade, dados):
        resultados = entidade.pegar_outra_tabela(dados.get("coluna"), dados.get("valor"), dados.get("tabela"), {"1": dados.get("1"), "2": dados.get("2")})
        return [resultado for resultado in resultados]



    def script(self):
        self.criar(
            self.pessoa,
            {
                "cpf": int("054740"),
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "honda1"
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": int("054743"),
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "honda1"
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": int("054744"),
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "honda1"
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": int("054741"),
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "honda2"
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": int("054742"),
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "honda3"
            },
        )
        self.criar(self.responsavel, {"pessoa": int("054740")})

        self.criar(self.professor, {"pessoa": int("054741"), "codigo": "#001"})
        self.criar(self.aluno, {"pessoa": int("054742")})
        self.criar(self.aluno, {"pessoa": int("054743")})
        self.criar(self.aluno, {"pessoa": int("054744")})
        self.criar(self.horario, {"codigo": 235})
        self.criar(self.modalidade, {"nome": "presencial"})

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
