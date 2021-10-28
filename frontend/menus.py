from opcoes import Opcoes
from pegar_dados import PegarDados


class Menu(PegarDados, Opcoes):
    def menu_aluno(self):
        self.opcoes_aluno().get(self.pega_entradas(self.tela_menu_aluno))()

    def menu_professor(self):
        self.opcoes_professor().get(self.pega_entradas(self.tela_menu_professor))()

    def menu_responsavel(self):
        self.opcoes_responsavel().get(self.pega_entradas(self.tela_menu_responsavel))()

    def menu_cadastro(self):
        self.opcoes_cadastro().get(self.pega_entradas(self.tela_quem_eh))()
        self.main()
