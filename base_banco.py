from conexao import Conexao
from entidades.alunos import Aluno
from entidades.experiencias import Experiencia, ExperienciaAtendeModalidade
from entidades.horarios import Horario
from entidades.livros import Livro
from entidades.modalidades import Modalidade
from entidades.notas import Nota
from entidades.pessoas import Pessoa
from entidades.procedures import Procedure
from entidades.professores import Professor
from entidades.responsaveis import Responsavel, ResponsavelPorAluno
from entidades.turmas import Turma, TurmaPossuiLivro
from entidades.unidades import Unidade
from scripts import Scripts

class EstruturaBase(Scripts):

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
    nota = Nota(conn)

    def __init__(self) -> None:
        Procedure(self.conn)
        self.scripts()

    def criar(self, entidade, dados):
        entidade.criar(dados)

    def deletar(self, entidade, dados):
        entidade.deletar(dados.get("coluna"), dados.get("valor"))

    def atualizar(self, entidade, dados):
        entidade.atualizar(dados)

    def pegar(self, entidade, dados=None, tudo=False, col_ordenar=None):
        resultados = (
            entidade.pegar(
                dados.get("coluna"), dados.get("valor"), col_ordenar=col_ordenar
            )
            if dados
            else entidade.pegar(tudo=tudo, col_ordenar=col_ordenar)
        )
        return [resultado for resultado in resultados]

    def pegar_outra_tabela(self, entidade, dados, col_ordenar=None):
        resultados = entidade.pegar_outra_tabela(
            dados.get("coluna"),
            dados.get("dado"),
            dados.get("tabela"),
            {"1": dados.get("1"), "2": dados.get("2")},
            col_ordenar=col_ordenar,
        )
        return [resultado for resultado in resultados]

    def inserir_imagem(self, path, dados):
        self.pessoa.inserir_imagem(path, dados)
