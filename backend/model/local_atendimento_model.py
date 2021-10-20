import connection.database as database

class LocalAtendimento:

    @staticmethod
    def ListarTodos():
        query_string = "SELECT * FROM local_atendimento"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        itens = cursor.fetchall()
        while itens:
            return itens
        connection.close()

    @staticmethod
    def InserirLocalAtendimento(nome_local, endereco, complemento, bairro, cep, cidade, uf):
        query_string = "INSERT INTO local_atendimento (nome_local, endereco, complemento, bairro, cep, cidade, uf) VALUES ('" + str(nome_local) + "' , '"+ str(endereco) +  "' , '"+ str(complemento) + "' , '"+ str(bairro) + "' , '"+ str(cep) + "' , '"+ str(cidade) + "' , '"+ str(uf) + "')"
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def EditarLocalAtendimento(id_local_atendimento, nome_local, endereco, complemento, bairro, cep, cidade, uf):
        query_string = "UPDATE local_atendimento SET nome_local = '" + str(nome_local) + "', endereco = '" + str(endereco) + "', complemento = '" + str(complemento) + "', bairro = '" + str(bairro) + "', cep = '" + str(cep) + "', cidade = '" + str(cidade) +  "', uf = '" + str(uf) + "' WHERE id_local_atendimento = " + str(id_local_atendimento) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

    @staticmethod
    def DeletarLocalAtendimento(id_local_atendimento):
        query_string = "DELETE FROM local_atendimento WHERE id_local_atendimento = " + str(id_local_atendimento) 
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        connection.close()

