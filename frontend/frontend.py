import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("./base_banco.py"), os.path.pardir)))

from base_banco import EstruturaBase



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Telas:
    tela_quem_eh = """
\tPara isso nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

Digite a opção desejada: """

    tela_inicial = f"""
        \t\tOlá! Seja bem vindo a nossa escola de idiomas!!

\tPara isso nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

* - Quero me cadastrar

Digite a opção desejada: """



class Frontend:
    def __init__(self) -> None:
        self.controller = EstruturaBase()
        self.cores = bcolors()
        self.telas = Telas()
        self.clear = lambda: os.system('clear')
        self.clear()
        self.principal()

    def pegar_dados_pessoa(self):
        return {
            "nome": self.pega_entradas("Digite seu nome: "),
            "cpf": self.pega_entradas("Digite seu cpf: "),
            "nascimento": self.pega_entradas("Digite sua nascimento: "),
            "sexo": self.pega_entradas("Digite seu sexo: "),
            "estado": self.pega_entradas("Digite seu estado: "),
            "cidade": self.pega_entradas("Digite sua cidade: "),
        }

    def pegar_dados_professor(self):
        return {
            "codigo": self.pega_entradas("Digite sua codigo"),
        }

    def opcoes_iniciais(self):
        return {
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.cadastro()
        }

    def opcoes_cadastro(self):
        return {
            "1": lambda: self.cadastra_pessoa_generica(self.controller.aluno),
            "2": lambda: self.cadastra_professor(),
            "3": lambda: self.cadastra_pessoa_generica(self.controller.responsavel),
        }

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
        self.clear()

    def cadastra_pessoa_generica(self, entidade):    
        self.controller.criar(entidade, {"cpf": self.cadastra_pessoa()})

    def pega_entradas(self, texto, is_int=False):
        entrada = input(self.cores.OKBLUE + texto + self.cores.ENDC)
        if is_int:
            return int(entrada)
        return entrada

    def principal(self):
        tela_inicial = self.telas.tela_inicial
        entrada = self.pega_entradas(tela_inicial)
        print(entrada, "-"*20)
        opcoes = self.opcoes_iniciais()
        opcoes.get(entrada)()

    def cadastro(self):
        self.opcoes_cadastro().get(self.pega_entradas(self.telas.tela_quem_eh))()
        self.principal()


a = Frontend()