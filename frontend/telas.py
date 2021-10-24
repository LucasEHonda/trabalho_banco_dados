import os.path

class Telas():
    tela_quem_eh = """
\tPara isso nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

Digite a opção desejada: """

    tela_inicial = """
        \t\tOlá! Seja bem vindo a nossa escola de idiomas!!

\tPara isso nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

* - Quero me cadastrar

Digite a opção desejada: """

    tela_menu_aluno = """
\tO que você deseja fazer:\n
1 - Consultar minha nota
2 - Consultar minha turma
3 - Consultar professores
4 - Ver meu perfil

Digite a opção desejada: """

    tela_menu_professor = """
\tO que você deseja fazer:\n
1 - Consultar minhas turmas
2 - Consultar aluno
3 - Consultar livros
4 - Ver meu perfil

Digite a opção desejada: """

    tela_menu_responsavel = """
\tO que você deseja fazer:\n
1 - Consultar meus dependentes
3 - Consultar professores
4 - Ver meu perfil

Digite a opção desejada: """

    def clear(self):
        os.system('clear')

class bcolors(Telas):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
