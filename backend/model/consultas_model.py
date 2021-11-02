import sqlite3
import connection.database as database


class Consultas:

    @staticmethod
    def ListarPorId(id):
        try:
            query_string = (
                "SELECT rowid, * FROM consultas WHERE rowid = " + str(id)
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
    def ListarPorMatricula(matricula_sus):
        try:
            query_string = (
                "SELECT * FROM pacientes where matricula_sus = " +
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
    def ListarTodos():
        try:
            query_string = "SELECT rowid, * FROM consultas"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirConsulta(
        matricula_sus,
        id_especialidade_medica,
        data_hora_marcada,
        id_medico,
        id_local_atendimento,
        compareceu
    ):
        try:
            query_string = (
                "INSERT INTO consultas (" +
                "matricula_sus, " +
                "id_especialidade_medica, " +
                "data_hora_marcada, " +
                "id_medico, " +
                "id_local_atendimento, " +
                "compareceu) " +
                "VALUES ('"
                + str(matricula_sus) + "','"
                + str(id_especialidade_medica) + "','"
                + str(data_hora_marcada) + "','"
                + str(id_medico) + "','"
                + str(id_local_atendimento) + "','"
                + str(compareceu) +
                "')"
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
    def EditarConsulta(
        id_consultas,
        matricula_sus,
        id_especialidade_medica,
        data_hora_marcada,
        id_medico,
        id_local_atendimento,
        compareceu
    ):
        try:
            query_string = (
                "UPDATE consultas SET " +
                " matricula_sus = '" + str(matricula_sus) +
                "', id_especialidade_medica = '" + str(id_especialidade_medica) +
                "', data_hora_marcada = '" + str(data_hora_marcada) +
                "', id_medico = '" + str(id_medico) +
                "', id_local_atendimento = '" + str(id_local_atendimento) +
                "', compareceu = '" + str(compareceu) +
                "' WHERE rowid = " + str(id_consultas)
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
    def DeletarConsulta(id_consultas):
        try:
            query_string = (
                "DELETE FROM consultas WHERE rowid = " + str(id_consultas)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
