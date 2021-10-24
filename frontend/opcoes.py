class Opcoes():   
    def opcoes_iniciais(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: self.menu_aluno(),
            "2": lambda: self.menu_professor(),
            "3": lambda: self.menu_responsavel(),
            "*": lambda: self.menu_cadastro(),
        }

    def opcoes_cadastro(self):
        return {
            "1": lambda: self.cadastra_pessoa_generica(self.controller.aluno),
            "2": lambda: self.cadastra_professor(),
            "3": lambda: self.cadastra_pessoa_generica(self.controller.responsavel),
        }

    def opcoes_aluno(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }        

    def opcoes_professor(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: self.cadastrar_turma(),
            "2": lambda: self.consultar_turmas(),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }

    def opcoes_responsavel(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: print("AINDA EM CONSTRUÇÃO"),
            "2": lambda: print("AINDA EM CONSTRUÇÃO"),
            "3": lambda: print("AINDA EM CONSTRUÇÃO"),
            "*": lambda: self.menu_cadastro()
        }
    