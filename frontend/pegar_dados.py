from telas import bcolors

class PegarDados(bcolors):
    def pegar_dados_login(self):
        return {
            "cpf": self.pega_entradas("Digite seu cpf: "),
            "senha": self.pega_entradas("Digite sua senha: "),
        }

    def pegar_dados_pessoa(self):
        dados = self.pegar_dados_login()
        dados.update(
            {
                "nome": self.pega_entradas("Digite seu nome: "),
                "aniversario": self.pega_entradas("Digite seu nascimento: "),
                "sexo": self.pega_entradas("Digite seu sexo: "),
                "estado": self.pega_entradas("Digite seu estado: "),
                "cidade": self.pega_entradas("Digite sua cidade: "),
            }
        )
        return dados

    def pegar_dados_professor(self):
        return {
            "codigo": self.pega_entradas("Digite seu codigo"),
        }

    def pegar_dados_turma(self):
        return {
            "codigo": self.pega_entradas("Digite o codigo da turma: "),
            "alunos": self.pega_entradas("Digite o CPF do aluno (PARA INSERIR MAIS DE UM ALUNO SIGA O EXEMPLO: 05472, 08111, 12345. PARA CADASTRAR APENAS UM ALUNO: 054742,): "),
            "horario": self.pega_entradas("Digite o horario: "),
            "modalidade": self.pega_entradas("Digite a modalidade: "),
        }

    def pega_entradas(self, texto, is_int=False):
        entrada = input(self.OKBLUE + texto + self.ENDC)
        if is_int:
            return int(entrada)
        return entrada    