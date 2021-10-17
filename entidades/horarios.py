
class Horario:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    codigo int PRIMARY KEY
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        codigo = dados.get("codigo")

        dados_inseridos = f"'{codigo}'"

        query = self.insert_query + f"(codigo) VALUES ({dados_inseridos});"

        try:
            self.mycursor.execute(query)
            print(f"^^^ Inserindo {dados_inseridos} na tabela tabela {self.CLASS_NAME} ^^^")
        except Exception as erro:
            print(f"Não foi possivel inserir em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}")        