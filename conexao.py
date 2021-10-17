import mysql.connector

class Conexao:
    def __init__(self) -> None:
        self.NOME_BANCO = 'db_escolaIdiomas'
        self.con = mysql.connector.connect(user='admin', password='admin123', host='localhost')

        self.mycursor = self.con.cursor()

        self.mycursor.execute("SHOW DATABASES")

        exists = False
        for x in self.mycursor:
            if (self.NOME_BANCO in list(x)):
                exists = True

        if not exists:
            print(f"--- Criando Banco {self.NOME_BANCO} ---")
            self.mycursor.execute(F"CREATE DATABASE {self.NOME_BANCO}")
        self.mycursor.execute(f"USE {self.NOME_BANCO}")
    
    def drop_banco(self) -> None:        
        self.mycursor.execute(f"DROP DATABASE {self.NOME_BANCO}")