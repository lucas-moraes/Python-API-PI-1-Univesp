import sqlite3
import backend.connection.database as database
from typing import Any


class Alergias:

    @staticmethod
    def ListarTodos() -> Any:
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
    def ListarPorId(id) -> Any:
        try:
            query_string = (
                "SELECT rowid, * FROM alergias WHERE rowid = " + str(id)
            )
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def ListarPorMatricula(matricula_sus) -> Any:
        try:
            query_string = (
                "SELECT * FROM alergias where matricula_sus = " +
                str(matricula_sus)
            )
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirAlergia(matricula_sus, descricao) -> Any:
        try:
            query_string = (
                "INSERT INTO alergias (matricula_sus, descricao) VALUES (" +
                str(matricula_sus) + " , '" + str(descricao) + "')"
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
    def EditarAlergia(id_alergias, descricao) -> Any:
        try:
            query_string = (
                "UPDATE alergias SET descricao = '" +
                str(descricao) + "' WHERE rowid = " +
                str(id_alergias)
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
    def DeletarAlergia(id_alergia) -> Any:
        try:
            query_string = (
                "DELETE FROM alergias WHERE rowid = " + str(id_alergia)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
