from conexao import Conexao
from entidades.pessoas import Pessoa
from entidades.professores import Professor
from entidades.turmas import Turma, TurmaPossuiLivro
from entidades.experiencias import Experiencia, ExperienciaAtendeModalidade
from entidades.modalidades import Modalidade
from entidades.responsaveis import Responsavel, ResponsavelPorAluno
from entidades.unidades import Unidade
from entidades.alunos import Aluno
from entidades.livros import Livro
from entidades.horarios import Horario

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