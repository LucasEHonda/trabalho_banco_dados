from .entidade_abstrata import EntidadeAbstrata


class Aluno(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    pessoa int PRIMARY KEY,
    foreign key (pessoa) references Pessoa(cpf) ON DELETE CASCADE,
    turma varchar(255),
    foreign key (turma) references Turma(codigo) ON DELETE CASCADE
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.conn = conn
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.conn.con.commit()

    def criar(self, dados):
        pessoa = dados.get("pessoa")

        dados_inseridos = f"{pessoa}"

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
