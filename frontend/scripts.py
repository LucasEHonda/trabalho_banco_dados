class Scripts:

    def criar_pessoas(self):
        self.criar(
            self.pessoa,
            {
                "cpf": 1,
                "aniversario": "07/12/1999",
                "nome": "Marco Aurelio1",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "responsavel1",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 2,
                "aniversario": "07/12/1999",
                "nome": "Marco Aurelio2",                
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "responsavel2",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 3,
                "aniversario": "07/12/1999",
                "nome": "Marco Aurelio3",                
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "responsavel3",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 4,
                "aniversario": "07/12/1999",
                "nome": "Marco Aurelio4",                
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "responsavel4",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 5,
                "aniversario": "07/12/1999",
                "nome": "Marco Aurelio5",                
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "responsavel5",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 6,
                "aniversario": "07/12/1999",
                "nome": "Maristela1",                
                "sexo": "Feminino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "professor1",
            },
        )        
        self.criar(
            self.pessoa,
            {
                "cpf": 7,
                "aniversario": "07/12/1999",
                "nome": "Maristela2",                
                "sexo": "Feminino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "professor2",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 8,
                "aniversario": "07/12/1999",
                "nome": "Maristela3",                
                "sexo": "Feminino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "professor3",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 9,
                "aniversario": "07/12/1999",
                "nome": "Maristela4",                
                "sexo": "Feminino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "professor4",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 10,
                "aniversario": "07/12/1999",
                "nome": "Maristela5",                
                "sexo": "Feminino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "professor5",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 11,
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda0",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "aluno1",
            },
        )        
        self.criar(
            self.pessoa,
            {
                "cpf": 12,
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda1",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "aluno2",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 13,
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda2",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "aluno3",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 14,
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda3",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "aluno4",
            },
        )
        self.criar(
            self.pessoa,
            {
                "cpf": 15,
                "aniversario": "07/12/1999",
                "nome": "Lucas Honda4",
                "sexo": "Masculino",
                "cidade": "Brasilia",
                "estado": "DF",
                "senha": "aluno5",
            },
        )                          
    def criar_responsavel(self):
        self.criar(self.responsavel, {"pessoa": 1})
        self.criar(self.responsavel, {"pessoa": 2})
        self.criar(self.responsavel, {"pessoa": 3})
        self.criar(self.responsavel, {"pessoa": 4})
        self.criar(self.responsavel, {"pessoa": 5})

    def criar_professor(self):
        self.criar(self.professor, {"pessoa": 6, "codigo": "#001"})
        self.criar(self.professor, {"pessoa": 7, "codigo": "#002"})
        self.criar(self.professor, {"pessoa": 8, "codigo": "#003"})
        self.criar(self.professor, {"pessoa": 9, "codigo": "#004"})
        self.criar(self.professor, {"pessoa": 10, "codigo": "#005"})

    def criar_aluno(self):
        self.criar(self.aluno, {"pessoa": 11})
        self.criar(self.aluno, {"pessoa": 12})
        self.criar(self.aluno, {"pessoa": 13})
        self.criar(self.aluno, {"pessoa": 14})
        self.criar(self.aluno, {"pessoa": 15})

    def criar_horario(self):
        self.criar(self.horario, {"codigo": 809})
        self.criar(self.horario, {"codigo": 910})
        self.criar(self.horario, {"codigo": 1011})
        self.criar(self.horario, {"codigo": 1112})
        self.criar(self.horario, {"codigo": 1213})

    def criar_modalidade(self):
        self.criar(self.modalidade, {"nome": "presencial"})
        self.criar(self.modalidade, {"nome": "semi-presencial"})
        self.criar(self.modalidade, {"nome": "EAD"})
        self.criar(self.modalidade, {"nome": "semi-EAD"})
        self.criar(self.modalidade, {"nome": "flexivel"})

    def criar_turma(self):
        self.criar(
            self.turma,
            {
                "codigo": "T1A - 35 - 809",
                "professor": 6,
                "horario": 809,
                "modalidade": "presencial",
            },
        )
        self.criar(
            self.turma,
            {
                "codigo": "T2A - 36 - 910",
                "professor": 7,
                "horario": 910,
                "modalidade": "semi-presencial",
            },
        )        
        self.criar(
            self.turma,
            {
                "codigo": "T3A - 37 - 1011",
                "professor": 8,
                "horario": 1011,
                "modalidade": "EAD",
            },
        )
        self.criar(
            self.turma,
            {
                "codigo": "T4A - 38 - 1112",
                "professor": 9,
                "horario": 1112,
                "modalidade": "semi-EAD",
            },
        )
        self.criar(
            self.turma,
            {
                "codigo": "T5A - 39 - 1213",
                "professor": 10,
                "horario": 1213,
                "modalidade": "flexivel",
            },
        )                    
    def criar_responsavel_por_aluno(self):
        self.criar(
            self.responsavel_por_aluno,
            {"aluno": 11, "responsavel": 1},
        )
        self.criar(
            self.responsavel_por_aluno,
            {"aluno": 12, "responsavel": 2},
        )
        self.criar(
            self.responsavel_por_aluno,
            {"aluno": 13, "responsavel": 3},
        )
        self.criar(
            self.responsavel_por_aluno,
            {"aluno": 14, "responsavel": 4},
        )
        self.criar(
            self.responsavel_por_aluno,
            {"aluno": 15, "responsavel": 5},
        )
                

    def criar_livro(self):
        self.criar(self.livro, {"nome": "T1A"})
        self.criar(self.livro, {"nome": "T2A"})
        self.criar(self.livro, {"nome": "T3A"})
        self.criar(self.livro, {"nome": "T4A"})
        self.criar(self.livro, {"nome": "T5A"})

    def atualizar_aluno(self):
        self.atualizar(
            self.aluno,
            {
                "coluna": "turma",
                "new":  "T1A - 35 - 809",
                "coluna_condicao": "pessoa",
                "valor_condicao": 11,
            },
        )
        self.atualizar(
            self.aluno,
            {
                "coluna": "turma",
                "new":  "T2A - 36 - 910",
                "coluna_condicao": "pessoa",
                "valor_condicao": 12,
            },
        )
        self.atualizar(
            self.aluno,
            {
                "coluna": "turma",
                "new":  "T3A - 37 - 1011",
                "coluna_condicao": "pessoa",
                "valor_condicao": 13,
            },
        )
        self.atualizar(
            self.aluno,
            {
                "coluna": "turma",
                "new": "T4A - 38 - 1112",
                "coluna_condicao": "pessoa",
                "valor_condicao": 14,
            },
        )        
        self.atualizar(
            self.aluno,
            {
                "coluna": "turma",
                "new": "T5A - 39 - 1213",
                "coluna_condicao": "pessoa",
                "valor_condicao": 15,
            },
        )        

    def scripts(self):
        self.criar_pessoas()
        self.criar_responsavel()
        self.criar_professor()
        self.criar_aluno()
        self.criar_horario()
        self.criar_modalidade()
        self.criar_turma()
        self.criar_responsavel_por_aluno()
        self.criar_livro()
        self.atualizar_aluno()
