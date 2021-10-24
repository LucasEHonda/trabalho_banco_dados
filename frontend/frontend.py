import sys
import os.path

from telas import bcolors
from menus import Menu

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("./base_banco.py"), os.path.pardir)))

from base_banco import EstruturaBase



class Frontend(Menu, bcolors):

    USER = None
    OPCAO_BASICA = None
    controller = EstruturaBase()

    def __init__(self) -> None:
        # self.clear()
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

    def cadastrar_turma(self):
        horarios = self.controller.pegar(self.controller.horario, tudo=True)
        modalidades = self.controller.pegar(self.controller.modalidade, tudo=True)

        if not horarios and not modalidades:
            print(self.FAIL + "Erro: Para cadastrar uma turma é preciso ter horario, e modalidade cadastrados no sistema" + self.FAIL)
            self.main()

        dados = self.pegar_dados_turma()
        
        dados.update({"professor": self.USER[0][0]})
        self.controller.criar(self.controller.turma, dados)    
        self.main()

    def consultar_turmas(self):
        turmas = self.controller.pegar(self.controller.turma, {"coluna": "professor", "valor": self.USER[0][0]})
        
        if turmas:
            for turma in turmas:
                print(f"TURMA: {turma[0]}\nAlunos:")
                print(f"Professor: {self.USER[0][2]}")
                print(f"Modalidade: {turma[4]}")
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
            pessoa_cpf = self.controller.pegar(self.controller.pessoa, {"coluna": "cpf", "valor": login.get("cpf")})
            pessoa_senha = self.controller.pegar(self.controller.pessoa, {"coluna": "senha", "valor": login.get("senha")})

            # self.clear()
            if (pessoa_senha and pessoa_senha) and (pessoa_senha == pessoa_cpf):
                print(self.OKGREEN + "Login realizado com sucesso" + self.OKGREEN)
                self.USER = pessoa_cpf
            else:
                print(self.FAIL + "Senha ou usuario invalido" + self.FAIL)
                self.main()
        opcoes.get(entrada)()


a = Frontend()