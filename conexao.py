import mysql.connector


class Conexao:

    NOME_BANCO = "db_escolaIdiomas"

    def __init__(self, user="admin", password="admin123", host="localhost") -> None:
        
        print(f"*** Iniciando conexão ao banco ***")
        self.con = mysql.connector.connect(
            user=user, password=password, host=host
        )

        self.mycursor = self.con.cursor()

        self.mycursor.execute("SHOW DATABASES")

        exists = False
        for x in self.mycursor:
            if self.NOME_BANCO in list(x):
                exists = True

        if not exists:
            print(f"--- Criando Banco {self.NOME_BANCO} ---")
            self.mycursor.execute(f"CREATE DATABASE {self.NOME_BANCO}")
        self.mycursor.execute(f"USE {self.NOME_BANCO}")

    def drop_banco(self) -> None:
        print(f"%%% Deletando banco {self.NOME_BANCO} %%%")
        self.mycursor.execute(f"DROP DATABASE {self.NOME_BANCO}")
