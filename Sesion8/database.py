import mysql.connector
import os

class MySQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            if(self.connection == None):
                os.system("color a2")
                self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.pw, database=self.db)
                
                print("Wow, me conecte satisfactoriamente")
        except mysql.ConnectionError as error:
            print("Error mientras se estaba conectando {}".format(error))
    
    def disconnect(self):
        try:
            if self. connections:
                self.connections.close
                self.connection = None
        except mysql.ConnectionError as error:
            print("Error")
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as error:
            print(f"Error : {error}")


db = MySQLDB("localhost", "root", "", "testlp")
print("Conectado")

db.connect()
categorias = db.execute_query("select * from categorias")

for reg in categorias:
    print(reg)
print(categorias)