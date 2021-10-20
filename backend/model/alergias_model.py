import connection.database as database

class Alergias:

    @staticmethod
    def ListarTodos():
        query_string = "SELECT * FROM alergias"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        itens = cursor.fetchall()
        while itens:
            return itens
        connection.close()

    @staticmethod
    def InserirAlergia(matricula_sus, descricao):
        query_string = "INSERT INTO alergias (matricula_sus, descricao) VALUES ('" + str(matricula_sus) + "' , '"+ str(descricao) + "')"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def EditarAlergia(id_alergias, descricao):
        query_string = "UPDATE alergias SET descricao = '" + str(descricao) + "' WHERE id_alergias = " + str(id_alergias) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def DeletarAlergia(id_alergia):
        query_string = "DELETE FROM alergias WHERE id_alergias = " + str(id_alergia) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

