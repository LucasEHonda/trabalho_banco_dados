import os.path

class Telas():
    tela_quem_eh = """
\tCADASTRO: Para isso nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

Digite a opção desejada: """

    tela_inicial = """
        \t\tOlá! Seja bem vindo a nossa escola de idiomas!!

\tPara começar nos diga quem você é:\n
1 - Aluno
2 - Professor
3 - Responsavel

* - Quero me cadastrar
0 - Sair

Digite a opção desejada: """

    tela_menu_aluno = """
        \t\tSeja bem-vindo aluno! O que deseja fazer?

\tO que você deseja fazer:\n
1 - Consultar minha nota
2 - Consultar minha turma
3 - Consultar professores
4 - Ver meu perfil

0 - Sair (Deslogar)

Digite a opção desejada: """

    tela_menu_professor = """
        \t\tSeja bem-vindo professor! O que deseja fazer?

\tO que você deseja fazer:\n
1 - Criar turma
2 - Adicionar alunos a turma
3 - Consultar minhas turmas
4 - Consultar aluno
5 - Consultar livros
6 - Criar horario
7 - Criar modalidade
8 - Ver meu perfil

0 - Sair (Deslogar)

Digite a opção desejada: """

    tela_menu_responsavel = """
        \t\tSeja bem-vindo responsavel! O que deseja fazer?

\tO que você deseja fazer:\n
1 - Consultar meus dependentes
3 - Consultar professores
4 - Ver meu perfil

0 - Sair (Deslogar)

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
