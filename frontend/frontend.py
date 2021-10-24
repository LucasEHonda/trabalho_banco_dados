import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("./base_banco.py"), os.path.pardir)))

from base_banco import EstruturaBase
from telas import bcolors
from menus import Menu



class Frontend(Menu, bcolors):
    def __init__(self) -> None:
        self.controller = EstruturaBase()
        self.clear()
        self.menu_principal()

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
        self.controller.criar(entidade, {"pessoa": self.cadastra_pessoa()})



a = Frontend()