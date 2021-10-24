from pegar_dados import PegarDados
from opcoes import Opcoes

class Menu(PegarDados, Opcoes):
    def menu_aluno():
        pass

    def menu_professor():
        pass

    def menu_responsavel():
        pass

    def menu_principal(self):
        entrada = self.pega_entradas(self.tela_inicial)
        opcoes = self.opcoes_iniciais()

    # try:
        opcoes.get(entrada)()
    # except:
        self.clear()
        print(self.FAIL + "ESSA OPÇÃO NÃO EXISTE.\n" + self.FAIL)
        self.menu_principal()

    def menu_cadastro(self):
        self.opcoes_cadastro().get(self.pega_entradas(self.tela_quem_eh))()
        self.menu_principal()