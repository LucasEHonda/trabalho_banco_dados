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

banco = EstruturaBase()

banco.pessoa.criar({"cpf": int('054742'), "aniversario": "07/12/1999" ,"nome": "Lucas Honda", "sexo": 'Masculino', "cidade": 'Brasilia', "estado": 'DF'})
banco.professor.criar({"pessoa": int('054742'), "codigo": "#001"})
banco.aluno.criar({"pessoa": int('054742')})
banco.unidade.criar({"professor": int('054742'), "nome": "brasilia - Asa sul"})
banco.responsavel.criar({"pessoa": int('054742')})
banco.horario.criar({"codigo": 235})
banco.livro.criar({"nome": 'como ser um cara legal'})
banco.modalidade.criar({"nome": 'presencial'})
banco.experiencia.criar({"nome": 'EAD'})
banco.turma.criar({"codigo": '#T01', "professor": int('054742'), "aluno": int('054742'), "horario": 235, "modalidade": 'presencial'})
banco.experiencia_atende_modalidade.criar({"modalidade": 'presencial', 'experiencia': 'EAD'})
banco.responsavel_por_aluno.criar({"aluno": int('054742'), "responsavel": int('054742')})
banco.turma_possui_livro.criar({'livro': 'como ser um cara legal', "turma": '#T01'})

banco.conn.drop_banco()