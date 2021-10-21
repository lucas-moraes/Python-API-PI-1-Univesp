import connection.database as database

class Consultas:

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT * FROM consultas"
            connection = database.connect()
            cursor = connection.cursor(as_dict = True)
            cursor.execute(query_string)
            for lista in cursor:
                return lista
        except:
            return False
        connection.close()

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
            query_string = ("INSERT INTO consultas (" + 
                "matricula_sus, " +
                "id_especialidade_medica, " +
                "data_hora_marcada, " +
                "id_medico, " +
                "id_local_atendimento, " +
                "compareceu) "+
                "VALUES ('" 
                    + str(matricula_sus) + "','"
                    + str(id_especialidade_medica) + "','"
                    + str(data_hora_marcada) + "','"
                    + str(id_medico) + "','"
                    + str(id_local_atendimento) + "','"
                    + str(compareceu) + 
                "')")
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
            query_string = ("UPDATE consultas SET " + 
                    " matricula_sus = '" + str(matricula_sus) + 
                    "', id_especialidade_medica = '" + str(id_especialidade_medica) + 
                    "', data_hora_marcada = '" + str(data_hora_marcada) + 
                    "', id_medico = '" + str(id_medico) + 
                    "', id_local_atendimento = '" + str(id_local_atendimento) + 
                    "', compareceu = '" + str(compareceu) + 
                "' WHERE id_consultas = " + str(id_consultas))
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
            query_string = "DELETE FROM consultas WHERE id_consultas = " + str(id_consultas) 
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
