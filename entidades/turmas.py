class Turma:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    codigo varchar(255) PRIMARY KEY,
    professor int NOT NULL,
    foreign key (professor) references Professor(pessoa),
    aluno int NOT NULL,
    foreign key (aluno) references Aluno(pessoa),
    horario int NOT NULL,
    foreign key (horario) references Horario(codigo),
    modalidade varchar(255) NOT NULL,
    foreign key (modalidade) references Modalidade(nome)
    );"""
        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        codigo = dados.get("codigo")
        professor = dados.get("professor")
        aluno = dados.get("aluno")
        horario = dados.get("horario")
        modalidade = dados.get("modalidade")

        dados_inseridos = (
            f"'{codigo}', '{professor}', '{aluno}', '{horario}', '{modalidade}'"
        )

        query = (
            self.insert_query
            + f"(codigo, professor, aluno, horario, modalidade) VALUES ({dados_inseridos});"
        )

        try:
            self.mycursor.execute(query)
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )


class TurmaPossuiLivro:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    livro varchar(255),
    foreign key (livro) references Livro(nome),
    turma varchar(255),
    foreign key (turma) references Turma(codigo)    
    );"""

        print(f"--- Criando/Instanciando tabela TurmaPossuiLivro ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        livro = dados.get("livro")
        turma = dados.get("turma")

        dados_inseridos = f"'{livro}', '{turma}'"

        query = self.insert_query + f"(livro, turma) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )
