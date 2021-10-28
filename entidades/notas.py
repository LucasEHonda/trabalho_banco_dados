from .entidade_abstrata import EntidadeAbstrata


class Nota(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    aluno int PRIMARY KEY,
    foreign key (aluno) references Aluno(pessoa) ON DELETE CASCADE,
    tipo varchar(255),
    nota varchar(255)
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        aluno = dados.get("aluno")
        tipo = dados.get("tipo")
        nota = dados.get("nota")

        dados_inseridos = f"{aluno}, '{tipo}', '{nota}'"

        query = self.insert_query + f"(aluno, tipo, nota) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )
