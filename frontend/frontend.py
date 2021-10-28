import os.path
import sys

from menus import Menu
from telas import bcolors

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("./base_banco.py"), os.path.pardir))
)

from base_banco import EstruturaBase


class Frontend(Menu, bcolors):

    USER = None
    OPCAO_BASICA = None
    controller = EstruturaBase()

    def __init__(self) -> None:
        # self.clear()
        # self.controller.conn.drop_banco()
        self.main()

    def cadastra_pessoa(self):

        dados = self.pegar_dados_pessoa()
        self.controller.criar(self.controller.pessoa, dados)

        return dados.get("cpf")

    def cadastra_professor(self):

        cpf = self.cadastra_pessoa()
        dados = self.pegar_dados_professor()
        dados.update({"pessoa": cpf})
        self.controller.criar(self.controller.professor, dados)

        self.pega_entradas("Aperte algo para ir para o menu iniciar")
        # self.clear()

    def cadastra_pessoa_generica(self, entidade):
        self.controller.criar(entidade, {"pessoa": self.cadastra_pessoa()})
        self.pega_entradas("Aperte algo para ir para o menu iniciar")
        # self.clear()

    def cadastrar_alunos_turma(self):
        flag = True

        if not self.controller.pegar(self.controller.turma, tudo=True):
            print(self.FAIL + "Erro: Não existem turmas cadastradas" + self.FAIL)
            self.main()

        turma = self.pega_entradas("Digite a turma que deseja inserir aluno(s): ")

        while flag:
            aluno = self.pega_entradas("Digite o cpf do aluno: ")
            self.controller.atualizar(
                self.controller.aluno,
                {
                    "coluna": "turma",
                    "new": turma,
                    "coluna_condicao": "pessoa",
                    "valor_condicao": aluno,
                },
            )
            flag = (
                False
                if self.pega_entradas(
                    "Deseja inserir mais alunos? (n/N parar ou qualquer tecla para continuar"
                )
                == ("n" or "N")
                else flag
            )

    def cadastrar_turma(self):
        horarios = self.controller.pegar(self.controller.horario, tudo=True)
        modalidades = self.controller.pegar(self.controller.modalidade, tudo=True)

        if not horarios and not modalidades:
            print(
                self.FAIL
                + "Erro: Para cadastrar uma turma é preciso ter horario, e modalidade cadastrados no sistema"
                + self.FAIL
            )
            self.main()

        dados = self.pegar_dados_turma()

        dados.update({"professor": self.USER[0][0]})
        self.controller.criar(self.controller.turma, dados)
        self.main()

    def cadastra_horario(self):
        self.controller.criar(self.controller.horario, self.pegar_dados_hoario())
        self.main()

    def cadastrar_nota(self):
        self.controller.criar(self.controller.nota, self.pegar_dados_nota())
        self.main()

    def cadastra_modalidade(self):
        self.controller.criar(self.controller.modalidade, self.pegar_dados_modalidade())
        self.main()

    def atualizar_foto_perfil(self):
        self.controller.inserir_imagem(
            path=self.pega_entradas("insira o caminho da imagem"), dados=self.USER[0][0]
        )
        self.main()

    def consultar_meu_perfil_professor(self):
        turmas = self.controller.pegar(
            self.controller.turma, {"coluna": "professor", "valor": self.USER[0][0]}
        )
        print(
            f"Professor: {self.USER[0][2]} {self.USER[0][5]}-{self.USER[0][6]}\nCPF: {self.USER[0][0]}\nSexo: {self.USER[0][3]}\nNascimento: {self.USER[0][4]}"
        )
        print("Suas turmas: ")
        for turma in turmas:
            print("\t\t" + turma[0], turma[3])

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_meu_perfil_aluno(self):
        aluno = self.controller.pegar(
            self.controller.aluno, {"coluna": "pessoa", "valor": self.USER[0][0]}
        )[0]
        turmas = self.controller.pegar(
            self.controller.turma, {"coluna": "codigo", "valor": aluno[1]}
        )
        pessoa = self.controller.pegar(
            self.controller.pessoa, {"coluna": "cpf", "valor": turmas[0][1]}
        )
        print(
            f"Aluno: {self.USER[0][2]} {self.USER[0][5]}-{self.USER[0][6]}\nCPF: {self.USER[0][0]}\nSexo: {self.USER[0][3]}\nNascimento: {self.USER[0][4]}"
        )
        print(
            "Sua turma:\t\t" + turmas[0][0],
            turmas[0][3],
            f"Horario: {turmas[0][2]}\nProfessor: {pessoa[0][2]}",
        )

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_meu_perfil_responsavel(self):
        responsavel = self.controller.pegar(
            self.controller.responsavel, {"coluna": "pessoa", "valor": self.USER[0][0]}
        )[0]
        responsavel_por_aluno = self.controller.pegar(
            self.controller.responsavel_por_aluno,
            {"coluna": "responsavel", "valor": responsavel[0]},
        )

        for aluno in responsavel_por_aluno:
            dependente = self.controller.pegar(
                self.controller.pessoa, {"coluna": "cpf", "valor": aluno[0]}
            )
            print(
                f"Responsavel: {self.USER[0][2]} {self.USER[0][5]}-{self.USER[0][6]}\nCPF: {self.USER[0][0]}\nSexo: {self.USER[0][3]}\nNascimento: {self.USER[0][4]}"
            )
            print("Seus dependentes:\t\t" + dependente[0][2])

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_meu_dependentes(self):
        responsavel_por_aluno = self.controller.pegar(
            self.controller.responsavel_por_aluno,
            {"coluna": "responsavel", "valor": self.USER[0][0]},
        )

        for aluno in responsavel_por_aluno:
            dependente = self.controller.pegar(
                self.controller.pessoa, {"coluna": "cpf", "valor": aluno[0]}
            )
            print("Seus dependentes:\t\t" + dependente[0][2])

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_minhas_notas(self):
        notas = self.controller.pegar(
            self.controller.nota, {"coluna": "aluno", "valor": self.USER[0][0]}
        )

        for nota in notas:
            print(f"{nota[1]}: {nota[2]}")

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_professores(self):
        turmas = self.controller.pegar(self.controller.turma, tudo=True)
        for turma in turmas:
            pessoa = self.controller.pegar(
                self.controller.pessoa, {"coluna": "cpf", "valor": turma[1]}
            )
            print(
                f"Professor: {pessoa[0][2]} {pessoa[0][5]}-{pessoa[0][6]}\nCPF: {pessoa[0][0]}\nSexo: {pessoa[0][3]}\nNascimento: {pessoa[0][4]}"
            )
            for turma in turmas:
                print("\t\t" + turma[0], turma[3], f"Horario: {turmas[0][2]}")

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_turma_aluno(self):
        aluno = self.controller.pegar(
            self.controller.aluno, {"coluna": "pessoa", "valor": self.USER[0][0]}
        )[0]
        turmas = self.controller.pegar(
            self.controller.turma, {"coluna": "codigo", "valor": aluno[1]}
        )
        pessoa = self.controller.pegar(
            self.controller.pessoa, {"coluna": "cpf", "valor": turmas[0][1]}
        )
        print(
            "Sua turma:\t\t" + turmas[0][0],
            turmas[0][3],
            f"Horario: {turmas[0][2]}\nProfessor: {pessoa[0][2]}",
        )

    def consultar_aluno(self):
        valor = self.pega_entradas("Digite o CPF do aluno: ", is_int=True)
        responsavel_por_aluno = self.controller.pegar(
            self.controller.responsavel_por_aluno, {"coluna": "aluno", "valor": valor}
        )
        alunos = self.controller.pegar_outra_tabela(
            self.controller.aluno,
            {
                "coluna": "pessoa",
                "dado": responsavel_por_aluno[0][0],
                "tabela": "Pessoa",
                "1": "pessoa",
                "2": "cpf",
            },
            "Pessoa.nome",
        )
        responsavel = self.controller.pegar_outra_tabela(
            self.controller.responsavel,
            {
                "coluna": "pessoa",
                "dado": responsavel_por_aluno[0][1],
                "tabela": "Pessoa",
                "1": "pessoa",
                "2": "cpf",
            },
            "Pessoa.nome",
        )

        print(
            f"Aluno: {alunos[0][4]} {alunos[0][7]}-{alunos[0][8]} turma: {alunos[0][1]}.\nResponsavel {responsavel[0][3]}."
        ) if alunos else print("algo")

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_livros(self):
        livros = self.controller.pegar(self.controller.livro, tudo=True)
        print(livros)

        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def consultar_turmas(self):
        turmas = self.controller.pegar(
            self.controller.turma, {"coluna": "professor", "valor": self.USER[0][0]}
        )

        if turmas:
            for turma in turmas:
                print(f"TURMA: {turma[0]}")
                print(f"Professor: {self.USER[0][2]}\nAlunos:")
                alunos = self.controller.pegar_outra_tabela(
                    self.controller.aluno,
                    {
                        "coluna": "turma",
                        "dado": turma[0],
                        "tabela": "Pessoa",
                        "1": "pessoa",
                        "2": "cpf",
                    },
                    "Pessoa.nome",
                )
                print("\tNOME -\t\t\tSEXO -\t\t\tNASCIMENTO")
                for aluno in alunos:
                    print(f"\t{aluno[4]} \t{aluno[5]} \t{aluno[6]}")
                print(f"Modalidade: {turma[3]}")
        else:
            print("Você não tem nenhuma turma cadastrada")
        self.pega_entradas("ENTER PARA IR PARA O MENU")
        self.main()

    def deslogar(self):
        self.USER = None
        self.OPCAO_BASICA = None

    def sair(self):
        return

    def main(self):
        opcoes = self.opcoes_iniciais()
        if self.USER:
            opcoes.get(self.OPCAO_BASICA)()

        entrada = self.pega_entradas(self.tela_inicial)
        self.OPCAO_BASICA = entrada

        if entrada != "*" and entrada != "0":
            print("Login")
            login = self.pegar_dados_login()
            pessoa_cpf = self.controller.pegar(
                self.controller.pessoa, {"coluna": "cpf", "valor": login.get("cpf")}
            )
            pessoa_senha = self.controller.pegar(
                self.controller.pessoa, {"coluna": "senha", "valor": login.get("senha")}
            )

            # self.clear()
            if (pessoa_senha and pessoa_senha) and (pessoa_senha == pessoa_cpf):
                print(self.OKGREEN + "Login realizado com sucesso" + self.OKGREEN)
                self.USER = pessoa_cpf
            else:
                print(self.FAIL + "Senha ou usuario invalido" + self.FAIL)
                self.main()
        opcoes.get(entrada)()


a = Frontend()
