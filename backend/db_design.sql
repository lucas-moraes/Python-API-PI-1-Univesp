CREATE TABLE pacientes
(
  id_paciente int NOT NULL IDENTITY(1,1),
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
);

CREATE TABLE alergias
(
  id_alergias int NOT NULL IDENTITY(1,1) PRIMARY KEY,
  matricula_sus bigint,
  descricao varchar(255)
);

CREATE TABLE consultas
(
  id_consultas int NOT NULL IDENTITY(1,1) PRIMARY KEY,
  matricula_sus bigint,
  id_especialidade_medica int,
  data_hora_marcada smalldatetime,
  id_medico int,
  id_local_atendimento int,
  compareceu varchar(5)
);

CREATE TABLE medicos
(
  id_medico int NOT NULL IDENTITY(1,1) PRIMARY KEY,
  crm int,
  nome varchar(255),
  sobrenome varchar(255),
  endereco varchar(255),
  complemento varchar(255),
  bairro varchar(255),
  cep varchar(8),
  cidade varchar(100),
  uf varchar(2),
  id_especialidade_medica int
);

CREATE TABLE especialidade_medica
(
  id_especialidade_medica INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
  desc_especialidade varchar(255)
);

CREATE TABLE local_atendimento
(
  id_local_atendimento INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
  nome_local varchar(255),
  endereco varchar(255),
  complemento varchar(255),
  bairro varchar(255),
  cep varchar(8),
  cidade varchar(255),
  UF varchar(2)
);

ALTER TABLE alergias ADD FOREIGN KEY (matricula_sus) REFERENCES pacientes (matricula_sus);

ALTER TABLE consultas ADD FOREIGN KEY (matricula_sus) REFERENCES pacientes (matricula_sus);

ALTER TABLE consultas ADD FOREIGN KEY (id_especialidade_medica) REFERENCES especialidade_medica (id_especialidade_medica);

ALTER TABLE consultas ADD FOREIGN KEY (id_medico) REFERENCES medicos (id_medico);

ALTER TABLE medicos ADD FOREIGN KEY (id_especialidade_medica) REFERENCES especialidade_medica (id_especialidade_medica);

ALTER TABLE consultas ADD FOREIGN KEY (id_local_atendimento) REFERENCES local_atendimento (id_local_atendimento);
