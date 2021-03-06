from .entidade_abstrata import EntidadeAbstrata


class Responsavel(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf) ON DELETE CASCADE
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.conn = conn
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.conn.con.commit()

    def criar(self, dados):
        professor = dados.get("pessoa")

        dados_inseridos = f"{professor}"

        query = self.insert_query + f"(pessoa) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )


class ResponsavelPorAluno(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    aluno int,
    foreign key (aluno) references Aluno(pessoa) ON DELETE CASCADE,
    responsavel int,
    foreign key (responsavel) references Responsavel(pessoa) ON DELETE CASCADE
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.conn = conn
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.conn.con.commit()

    def criar(self, dados):
        aluno = dados.get("aluno")
        responsavel = dados.get("responsavel")

        dados_inseridos = f"{aluno}, '{responsavel}'"

        query = self.insert_query + f"(aluno, responsavel) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            self.conn.con.commit()
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )
