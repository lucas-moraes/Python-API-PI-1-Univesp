import sqlite3
import connection.database as database


class Medicos:

    @staticmethod
    def ListarPorId(id):
        try:
            query_string = (
                "SELECT rowid, * FROM medicos WHERE rowid =" + str(id))
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
            query_string = "SELECT rowid, * FROM medicos"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirMedico(
        crm,
        nome,
        sobrenome,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf,
        id_especialidade_medica
    ):
        try:
            query_string = (
                "INSERT INTO medicos (" +
                "crm" +
                ", nome" +
                ", sobrenome" +
                ", endereco" +
                ", complemento" +
                ", bairro" +
                ", cep" +
                ", cidade" +
                ", uf" +
                ", id_especialidade_medica) " +
                "VALUES ("
                + str(crm) + " , '"
                + str(nome) + "' , '"
                + str(sobrenome) + "' , '"
                + str(endereco) + "' , '"
                + str(complemento) + "' , '"
                + str(bairro) + "' , '"
                + str(cep) + "' , '"
                + str(cidade) + "' , '"
                + str(uf) + "' , "
                + str(id_especialidade_medica) +
                ")"
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
    def EditarMedico(
        id,
        crm,
        nome,
        sobrenome,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf,
        id_especialidade_medica
    ):
        try:
            query_string = (
                "UPDATE medicos SET " +
                "crm = " + str(crm) +
                ", nome = '" + str(nome) +
                "', sobrenome = '" + str(sobrenome) +
                "', endereco = '" + str(endereco) +
                "', complemento = '" + str(complemento) +
                "', bairro = '" + str(bairro) +
                "', cep = '" + str(cep) +
                "', cidade = '" + str(cidade) +
                "', uf = '" + str(uf) +
                "', id_especialidade_medica = " + str(id_especialidade_medica) +
                " WHERE rowid = " + str(id)
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
    def DeletarMedico(
        id_medico
    ):
        try:
            query_string = (
                "DELETE FROM medicos WHERE rowid = " + str(id_medico)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
