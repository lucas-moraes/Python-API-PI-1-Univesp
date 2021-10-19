import connection.database as database

class EspecialidadeMedica:

    @staticmethod
    def ListarTodos():
        query_string = "SELECT * FROM especialidade_medica"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        itens = cursor.fetchall()
        while itens:
            return itens
        connection.close()

    @staticmethod
    def InserirEspecialidade(desc_especialidade):
        query_string = "INSERT INTO especialidade_medica (desc_especialidade) VALUES ('" + str(desc_especialidade) + "')"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def DeletarEspecialidade(id_especialidade_medica):
        query_string = "DELETE FROM especialidade_medica WHERE id_especialidade_medica = " + str(id_especialidade_medica) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

