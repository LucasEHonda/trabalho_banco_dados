from telas import bcolors

class PegarDados(bcolors):
    def pegar_dados_pessoa(self):
        return {
            "nome": self.pega_entradas("Digite seu nome: "),
            "cpf": self.pega_entradas("Digite seu cpf: "),
            "aniversario": self.pega_entradas("Digite seu nascimento: "),
            "sexo": self.pega_entradas("Digite seu sexo: "),
            "estado": self.pega_entradas("Digite seu estado: "),
            "cidade": self.pega_entradas("Digite sua cidade: "),
        }

    def pegar_dados_professor(self):
        return {
            "codigo": self.pega_entradas("Digite sua codigo"),
        }

    def pega_entradas(self, texto, is_int=False):
        entrada = input(self.OKBLUE + texto + self.ENDC)
        if is_int:
            return int(entrada)
        return entrada    