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
            "codigo": self.pega_entradas("Digite seu codigo: "),
        }

    def pegar_dados_hoario(self):
        return {
            "codigo": self.pega_entradas("Digite o codigo: "),
        }

    def pegar_dados_nota(self):
        return {
            "aluno": self.pega_entradas("Digite o CPF do aluno: "),
            "tipo": self.pega_entradas(
                "Digite o tipo da nota (exemplo: atividade, prova, trabalho): "
            ),
            "nota": self.pega_entradas("Digite a nota do aluno: "),
        }

    def pegar_dados_modalidade(self):
        return {
            "nome": self.pega_entradas("Digite a modalidade: "),
        }

    def pegar_dados_turma(self):
        return {
            "codigo": self.pega_entradas("Digite o codigo da turma: "),
            "horario": self.pega_entradas("Digite o horario: "),
            "modalidade": self.pega_entradas("Digite a modalidade: "),
        }

    def pegar_dados_deletar_turma(self):
        return  {"codigo": self.pega_entradas("Digite o codigo da turma: "),}

    def pega_entradas(self, texto, is_int=False):
        entrada = input(self.OKBLUE + texto + self.ENDC)
        if is_int:
            return int(entrada)
        return entrada
