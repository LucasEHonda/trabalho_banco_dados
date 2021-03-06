from .entidade_abstrata import EntidadeAbstrata


class Livro(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__
        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "
        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    nome varchar(255) PRIMARY KEY
    );"""
        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.conn = conn
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.conn.con.commit()

    def criar(self, dados):
        nome = dados.get("nome")

        dados_inseridos = f"'{nome}'"

        query = self.insert_query + f"(nome) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            print(
                f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^"
            )
        except Exception as erro:
            print(
                f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )
