class EntidadeAbstrata:

    debug = False

    def __init__(self, conn, debug=False) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} ("""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.debug = debug

    def criar(self, dados):
        pass

    def deletar(self, coluna, dado):
        query = f"DELETE FROM {self.CLASS_NAME} WHERE {coluna}='{dado}';"

        try:
            self.mycursor.execute(query)
            print(
                f"%%% Deletando {dado} na tabela tabela {self.CLASS_NAME} %%%"
            ) if self.debug else None
        except Exception as erro:
            print(
                f"Não foi possivel deletar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            ) if self.debug else None

    def atualizar(self, dados):
        query = f'UPDATE {self.CLASS_NAME} SET {dados.get("coluna")}="{dados.get("new")}" where {dados.get("coluna_condicao")}={dados.get("valor_condicao")};'

        try:
            self.mycursor.execute(query)
            print(
                f'@@@ Atualizando {dados.get("coluna")} na tabela tabela {self.CLASS_NAME} @@@'
            ) if self.debug else None
        except Exception as erro:
            print(
                f"Não foi possivel atualizar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            ) if self.debug else None

    def pegar(self, coluna=None, dado=None, tudo=False, col_ordenar=None):
        ordenar = f" ORDER BY {col_ordenar};"
        base = f"SELECT * FROM {self.CLASS_NAME}"
        query = base + f" WHERE {coluna}='{dado}'" if not tudo else base
        query = query + ordenar if col_ordenar else query + ";"

        try:
            self.mycursor.execute(query)
            print(
                f"%%% Pegando {dado} na tabela tabela {self.CLASS_NAME} %%%"
            ) if self.debug else None
        except Exception as erro:
            print(
                f"Não foi possivel pegar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
                if self.debug
                else None
            )

        return self.mycursor.fetchall()

    def pegar_outra_tabela(self, coluna, dado, tabela, ids, col_ordenar=None):
        ordenar = f" ORDER BY {col_ordenar};"
        primary_id = ids.get("1")
        second_id = ids.get("2")
        query = f"SELECT * FROM {self.CLASS_NAME} INNER JOIN {tabela} ON {self.CLASS_NAME}.{primary_id} = {tabela}.{second_id} WHERE {coluna}='{dado}'"
        query = query + ordenar if col_ordenar else query + ";"

        try:
            self.mycursor.execute(query)
            print(
                f"%%% Pegando {dado} na tabela tabela {self.CLASS_NAME} %%%"
            ) if self.debug else None
        except Exception as erro:
            print(
                f"Não foi possivel pegar em {self.CLASS_NAME}. Ocorreu o seguinte erro>> {erro}"
            ) if self.debug else None

        return self.mycursor.fetchall()

    def inserir_imagem(self, path, dados):
        binaryData = open(path, "rb").read()

        query = "UPDATE Pessoa SET imagem=%s where cpf=%s;"
        self.mycursor.execute(
            query,
            (
                binaryData,
                dados,
            ),
        )
