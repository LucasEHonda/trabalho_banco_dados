import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("./base_banco.py"), os.path.pardir)))

from base_banco import EstruturaBase

class Opcoes():
    def __init__(self) -> None:
        self.controller = EstruturaBase()    

    def opcoes_iniciais(self):
        return {
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }

    def opcoes_cadastro(self):
        return {
            "1": lambda: self.cadastra_pessoa_generica(self.controller.aluno),
            "2": lambda: self.cadastra_professor(),
            "3": lambda: self.cadastra_pessoa_generica(self.controller.responsavel),
        }

    def opcoes_aluno(self):
        return {
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }        

    def opcoes_professor(self):
        return {
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }

    def opcoes_responsavel(self):
        return {
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }
    