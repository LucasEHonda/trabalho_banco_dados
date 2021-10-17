class Experiencia:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    nome varchar(255) PRIMARY KEY
    );"""

        print(f"--- Criando/Instanciando tabela {self.CLASS_NAME} ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

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


class ExperienciaAtendeModalidade:
    def __init__(self, conn) -> None:
        self.CLASS_NAME = self.__class__.__name__

        self.insert_query = f"INSERT INTO {self.CLASS_NAME} "

        query = f"""CREATE TABLE IF NOT EXISTS {self.CLASS_NAME} (
    modalidade varchar(255) NOT NULL,
    foreign key (modalidade) references Modalidade(nome),
    experiencia varchar(255) NOT NULL,
    foreign key (experiencia) references Experiencia(nome)
    );"""

        print(f"--- Criando/Instanciando tabela ExperienciaAtendeModalidade ---")

        self.mycursor = conn.mycursor
        self.mycursor.execute(query)

    def criar(self, dados):
        modalidade = dados.get("modalidade")
        experiencia = dados.get("experiencia")

        dados_inseridos = f"'{modalidade}', '{experiencia}'"

        query = (
            self.insert_query + f"(modalidade, experiencia) VALUES ({dados_inseridos});"
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
