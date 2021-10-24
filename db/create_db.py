import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"banco_de_dados.db"

    sql_create_pacientes_table = """ CREATE TABLE IF NOT EXISTS pacientes (
                                        matricula_sus bigint NOT NULL PRIMARY KEY,
                                        data_registro smalldatetime,
                                        tipo_sangue varchar(3),
                                        nome varchar(50),
                                        sobrenome varchar(255),
                                        data_nasc date,
                                        endereco varchar(255),
                                        complemento varchar(255),
                                        bairro varchar(255),
                                        cep varchar(8),
                                        cidade varchar(100),
                                        uf varchar(2)
                                    ); """

    sql_create_alergias_table = """CREATE TABLE IF NOT EXISTS alergias (
                                    matricula_sus bigint,
                                    descricao varchar(255),
                                    FOREIGN KEY (matricula_sus) REFERENCES pacientes (matricula_sus)
                                );"""

    sql_create_consultas_table = """CREATE TABLE IF NOT EXISTS consultas (
                                        matricula_sus bigint,
                                        id_especialidade_medica int,
                                        data_hora_marcada smalldatetime,
                                        id_medico int,
                                        id_local_atendimento int,
                                        compareceu varchar(5),
                                        FOREIGN KEY (matricula_sus) REFERENCES pacientes (matricula_sus),
                                        FOREIGN KEY (id_especialidade_medica) REFERENCES especialidade_medica (id_especialidade_medica),
                                        FOREIGN KEY (id_medico) REFERENCES medicos (id_medico),
                                        FOREIGN KEY (id_local_atendimento) REFERENCES local_atendimento (id_local_atendimento)
                                    );"""

    sql_create_medicos_table = """CREATE TABLE IF NOT EXISTS medicos (
                                    crm int,
                                    nome varchar(255),
                                    sobrenome varchar(255),
                                    endereco varchar(255),
                                    complemento varchar(255),
                                    bairro varchar(255),
                                    cep varchar(8),
                                    cidade varchar(100),
                                    uf varchar(2),
                                    id_especialidade_medica int,
                                    FOREIGN KEY (id_especialidade_medica) REFERENCES especialidade_medica (id_especialidade_medica)
                                );"""

    sql_create_especialidade_medica_table = """CREATE TABLE IF NOT EXISTS especialidade_medica (
                                                desc_especialidade varchar(255)
                                            );"""

    sql_create_local_atendimento_table = """CREATE TABLE IF NOT EXISTS local_atendimento (
                                                nome_local varchar(255),
                                                endereco varchar(255),
                                                complemento varchar(255),
                                                bairro varchar(255),
                                                cep varchar(8),
                                                cidade varchar(255),
                                                uf varchar(2)
                                            );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_pacientes_table)
        create_table(conn, sql_create_alergias_table)
        create_table(conn, sql_create_consultas_table)
        create_table(conn, sql_create_medicos_table)
        create_table(conn, sql_create_especialidade_medica_table)
        create_table(conn, sql_create_local_atendimento_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
