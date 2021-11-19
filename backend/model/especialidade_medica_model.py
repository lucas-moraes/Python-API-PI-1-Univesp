import backend.connection.database as database


class EspecialidadeMedica:

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT * FROM especialidade_medica"
            connection = database.connect()
            cursor = connection.cursor(as_dict=True)
            cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False
        connection.close()

    @staticmethod
    def InserirEspecialidade(
        desc_especialidade
    ):
        try:
            query_string = "INSERT INTO especialidade_medica (desc_especialidade) VALUES ('" + str(
                desc_especialidade) + "')"
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
            query_string = "UPDATE especialidade_medica SET desc_especialidade = '" + \
                str(desc_especialidade) + "' WHERE id_especialidade_medica = " + \
                str(id_especialidade_medica)
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
            query_string = "DELETE FROM especialidade_medica WHERE id_especialidade_medica = " + \
                str(id_especialidade_medica)
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
