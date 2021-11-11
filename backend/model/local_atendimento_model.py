import sqlite3
import backend.connection.database as database


class LocalAtendimento:

    @staticmethod
    def ListarPorId(id):
        try:
            query_string = (
                "SELECT rowid, * FROM local_atendimento WHERE rowid =" +
                str(id)
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
            query_string = "SELECT rowid, * FROM local_atendimento"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirLocalAtendimento(
        nome_local,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf
    ):
        try:
            query_string = (
                "INSERT INTO local_atendimento " +
                "(nome_local, endereco, complemento, bairro, cep, cidade, uf) " +
                "VALUES ('" +
                str(nome_local) + "' , '" +
                str(endereco) + "' , '" +
                str(complemento) + "' , '" +
                str(bairro) + "' , '" +
                str(cep) + "' , '" +
                str(cidade) + "' , '" +
                str(uf) +
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
    def EditarLocalAtendimento(
        id_local_atendimento,
        nome_local,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf
    ):
        try:
            query_string = (
                "UPDATE local_atendimento SET " +
                "nome_local = '" + str(nome_local) +
                "', endereco = '" + str(endereco) +
                "', complemento = '" + str(complemento) +
                "', bairro = '" + str(bairro) +
                "', cep = '" + str(cep) +
                "', cidade = '" + str(cidade) +
                "', uf = '" + str(uf) +
                "' WHERE rowid = " +
                str(id_local_atendimento)
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
    def DeletarLocalAtendimento(
        id_local_atendimento
    ):
        try:
            query_string = (
                "DELETE FROM local_atendimento WHERE rowid = " +
                str(id_local_atendimento)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
