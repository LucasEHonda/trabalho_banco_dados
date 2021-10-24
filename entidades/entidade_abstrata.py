class EntidadeAbstrata:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} ("""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        pass

    def deletar(self, coluna, dado):
        query = f"DELETE FROM {self.CLASS_NAME} WHERE {coluna}='{dado}';"

        try:
            self.mycursor.execute(query)
            print(f"%%% Deletando {dado} na tabela tabela {self.CLASS_NAME} %%%")
        except Exception as erro:
            print(
                f"Não foi possivel deletar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )

    def pegar(self, coluna=None, dado=None, tudo=False):
        base = f"SELECT * FROM {self.CLASS_NAME}"
        query = base + f" WHERE {coluna}='{dado}';" if not tudo else base

        try:
            self.mycursor.execute(query)
            print(f"%%% Pegando {dado} na tabela tabela {self.CLASS_NAME} %%%")
        except Exception as erro:
            print(
                f"Não foi possivel pegar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )

        return self.mycursor.fetchall()

    def pegar_outra_tabela(self, coluna, dado, tabela, ids):
        primary_id = ids.get('1')
        second_id = ids.get('2')
        query = f"SELECT * FROM {self.CLASS_NAME} INNER JOIN {tabela} ON {self.CLASS_NAME}.{primary_id} = {tabela}.{second_id} WHERE {coluna}='{dado}';"

        try:
            self.mycursor.execute(query)
            print(f"%%% Pegando {dado} na tabela tabela {self.CLASS_NAME} %%%")
        except Exception as erro:
            print(
                f"Não foi possivel pegar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            )

        return self.mycursor.fetchall()