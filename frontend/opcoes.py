class Opcoes:
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
            "1": lambda: self.consultar_minhas_notas(),
            "2": lambda: self.consultar_turma_aluno(),
            "3": lambda: self.consultar_professores(),
            "4": lambda: self.atualizar_foto_perfil(),
            "5": lambda: self.consultar_meu_perfil_aluno(),
            "*": lambda: self.menu_cadastro(),
        }

    def opcoes_professor(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: self.cadastrar_turma(),
            "2": lambda: self.cadastrar_alunos_turma(),
            "3": lambda: self.consultar_turmas(),
            "4": lambda: self.consultar_aluno(),
            "5": lambda: self.consultar_livros(),
            "6": lambda: self.cadastra_horario(),
            "7": lambda: self.cadastra_modalidade(),
            "8": lambda: self.cadastrar_nota(),
            "9": lambda: self.atualizar_foto_perfil(),
            "10": lambda: self.consultar_meu_perfil_professor(),
        }
    
    def opcoes_minhas_turmas_professor(self):
        return {
            "0": lambda: self.main(),
            "1": lambda: print("Opção em construção!!!"),
            "2": lambda: print("Opção em construção!!!"),
            "3": lambda: print("Opção em construção!!!"),
            "4": lambda: self.deletar_turma(),
        }

    def opcoes_responsavel(self):
        return {
            "0": lambda: self.sair(),
            "1": lambda: self.consultar_meu_dependentes(),
            "2": lambda: self.consultar_professores(),
            "3": lambda: self.atualizar_foto_perfil(),
            "4": lambda: self.consultar_meu_perfil_responsavel(),
            "*": lambda: self.menu_cadastro(),
        }
