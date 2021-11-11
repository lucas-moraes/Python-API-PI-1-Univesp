import sqlite3
import backend.connection.database as database


class Pacientes:

    @staticmethod
    def ListarPorId(id):
        try:
            query_string = (
                "SELECT rowid, * FROM pacientes WHERE rowid =" + str(id)
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
            listagem = cursor.fetchone()
            return listagem
        except:
            return False

    @staticmethod
    def ListarTodos():
        try:
            query_string = "SELECT rowid, * FROM pacientes"
            connection = database.connect()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            listagem = cursor.execute(query_string)
            listagem = cursor.fetchall()
            return listagem
        except:
            return False

    @staticmethod
    def InserirPaciente(
        matricula_sus,
        data_registro,
        tipo_sangue,
        nome,
        sobrenome,
        data_nasc,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf
    ):
        try:
            query_string = (
                "INSERT INTO pacientes (" +
                "matricula_sus" +
                ", data_registro" +
                ", tipo_sangue" +
                ", nome" +
                ", sobrenome" +
                ", data_nasc" +
                ", endereco" +
                ", complemento" +
                ", bairro" +
                ", cep" +
                ", cidade" +
                ", uf) " +
                "VALUES ("
                + str(matricula_sus) + " , '"
                + str(data_registro) + "' , '"
                + str(tipo_sangue) + "' , '"
                + str(nome) + "' , '"
                + str(sobrenome) + "' , '"
                + str(data_nasc) + "' , '"
                + str(endereco) + "' , '"
                + str(complemento) + "' , '"
                + str(bairro) + "' , '"
                + str(cep) + "' , '"
                + str(cidade) + "' , '"
                + str(uf) +
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
    def EditarPaciente(
        id,
        matricula_sus,
        data_registro,
        tipo_sangue,
        nome,
        sobrenome,
        data_nasc,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf
    ):
        try:
            query_string = (
                "UPDATE pacientes SET " +
                "matricula_sus = " + str(matricula_sus) +
                ", data_registro = '" + str(data_registro) +
                "', tipo_sangue = '" + str(tipo_sangue) +
                "', nome = '" + str(nome) +
                "', sobrenome = '" + str(sobrenome) +
                "', data_nasc = '" + str(data_nasc) +
                "', endereco = '" + str(endereco) +
                "', complemento = '" + str(complemento) +
                "', bairro = '" + str(bairro) +
                "', cep = '" + str(cep) +
                "', cidade = '" + str(cidade) +
                "', uf = '" + str(uf) +
                "' WHERE rowid = " + str(id)
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
    def DeletarPaciente(id_paciente):
        try:
            query_string = (
                "DELETE FROM pacientes WHERE rowid = " + str(id_paciente)
            )
            connection = database.connect()
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()
            connection.close()
            return True
        except:
            return False
