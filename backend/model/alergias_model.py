import sqlite3
import connection.database as database


class Alergias:

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT rowid, * FROM alergias"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def ListarAlergiasPorMatricula(matricula_sus):
        print(matricula_sus)
        try:
            query_string = "SELECT * FROM alergias where matricula_sus=" + \
                str(matricula_sus)
            connection = database.connect()
            cursor = connection.cursor(as_dict=True)
            cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirAlergia(matricula_sus, descricao):
        try:
            query_string = "INSERT INTO alergias (matricula_sus, descricao) VALUES (" + str(
                matricula_sus) + " , '" + str(descricao) + "')"
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
            query_string = "UPDATE alergias SET descricao = '" + \
                str(descricao) + "' WHERE rowid = " + str(id_alergias)
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
            query_string = "DELETE FROM alergias WHERE rowid = " + \
                str(id_alergia)
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
