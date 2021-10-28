from .entidade_abstrata import EntidadeAbstrata


class Pessoa(EntidadeAbstrata):
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    cpf int PRIMARY KEY,
    senha varchar(255)  NOT NULL,
    nome varchar(255)  NOT NULL,
    sexo varchar(10)  NOT NULL,
    imagem BLOB,
    aniversario varchar(10)  NOT NULL,
    cidade varchar(255)  NOT NULL,
    estado varchar(255)  NOT NULL
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.conn = conn
        self.mycursor = conn.mycursor
        self.mycursor.execute(query)
        self.conn.con.commit()

    def criar(self, dados):
        cpf = dados.get("cpf")
        nome = dados.get("nome")
        sexo = dados.get("sexo")
        aniversario = dados.get("aniversario")
        cidade = dados.get("cidade")
        estado = dados.get("estado")
        senha = dados.get("senha")

        dados_inseridos = f"{cpf}, '{senha}', '{nome}', '{sexo}', '{aniversario}', '{cidade}', '{estado}'"

        query = (
            self.insert_query
            + f"(cpf, senha, nome, sexo, aniversario, cidade, estado) VALUES ({dados_inseridos});"
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
