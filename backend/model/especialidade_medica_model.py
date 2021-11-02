import sqlite3
import connection.database as database


class EspecialidadeMedica:

    @staticmethod
    def ListarPorId(id):
        try:
            query_string = (
                "SELECT rowid, * FROM especialidade_medica WHERE rowid = " +
                str(id)
            )
            print(query_string)
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT rowid, * FROM especialidade_medica"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirEspecialidade(
        desc_especialidade
    ):
        try:
            query_string = (
                "INSERT INTO especialidade_medica (desc_especialidade) VALUES ('" +
                str(desc_especialidade) + "')"
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False

    @staticmethod
    def EditarEspecialidade(
        id_especialidade_medica,
        desc_especialidade
    ):
        try:
            query_string = (
                "UPDATE especialidade_medica SET desc_especialidade = '" +
                str(desc_especialidade) + "' WHERE rowid = " +
                str(id_especialidade_medica)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False

    @staticmethod
    def DeletarEspecialidade(
        id_especialidade_medica
    ):
        try:
            query_string = (
                "DELETE FROM especialidade_medica WHERE rowid = " +
                str(id_especialidade_medica)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
