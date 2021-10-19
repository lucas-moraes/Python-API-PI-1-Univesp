import pymssql 

def connect():
    try:
        connection = pymssql.connect(server='localhost', user='SA', password='@a1b2c3d4e5', database='TestDB')  
        return connection
    except:
        print("Erro na conexão")

