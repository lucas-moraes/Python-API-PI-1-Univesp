import connection.database as database

class Medicos:

    @staticmethod
    def ListarTodos():
        query_string = "SELECT * FROM medicos"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        itens = cursor.fetchall()
        while itens:
            return itens
        connection.close()

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
        query_string = ("INSERT INTO medicos (" + 
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
            ")")
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

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
        query_string = ("UPDATE medicos SET " + 
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
            " WHERE id_medico = " + str(id) )
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def DeletarMedico(id_medico):
        query_string = "DELETE FROM medicos WHERE id_medico = " + str(id_medico) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()