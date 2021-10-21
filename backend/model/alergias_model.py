import connection.database as database

class Alergias:

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT * FROM alergias"
            connection = database.connect()
            cursor = connection.cursor(as_dict = True)
            cursor.execute(query_string)
            for lista in cursor:
                return lista
        except:
            return False
        connection.close()

    @staticmethod
    def InserirAlergia(matricula_sus, descricao):
        try:
            query_string = "INSERT INTO alergias (matricula_sus, descricao) VALUES (" + str(matricula_sus) + " , '"+ str(descricao) + "')"
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False

    @staticmethod
    def EditarAlergia(id_alergias, descricao):
        try:
            query_string = "UPDATE alergias SET descricao = '" + str(descricao) + "' WHERE id_alergias = " + str(id_alergias) 
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
            
    @staticmethod
    def DeletarAlergia(id_alergia):
        try:
            query_string = "DELETE FROM alergias WHERE id_alergias = " + str(id_alergia) 
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False


