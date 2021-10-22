from model import alergias_model
from model import consultas_model
from model import especialidade_medica_model
from model import local_atendimento_model
from model import medicos_model
from model import pacientes_model

class Update:

    @staticmethod
    def EditarAlergia(
        id_alergias, 
        descricao
    ):
        do = alergias_model.Alergias()
        response = do.EditarAlergia(
            id_alergias, 
            descricao
        )
        return response

    @staticmethod
    def EditarConsulta(
        id_consultas, 
        matricula_sus, 
        id_especialidade_medica, 
        data_hora_marca, 
        id_medico, 
        id_local_atendimento, 
        compareceu
    ):
        do = consultas_model.Consultas()
        response = do.EditarConsulta(
            id_consultas, 
            matricula_sus, 
            id_especialidade_medica, 
            data_hora_marca, 
            id_medico, 
            id_local_atendimento, 
            compareceu
        )
        return response

    @staticmethod
    def EditarEspecialidadeMedica(
        id_especialidade_medica, 
        desc_especialidade
    ):
        do = especialidade_medica_model.Alergias()
        response = do.EditarEspecialidadeMedica(
            id_especialidade_medica, 
            desc_especialidade
        )
        return response

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
        do = local_atendimento_model.LocalAtendimento()
        response = do.EditarLocalAtendimento(
            id_local_atendimento, 
            nome_local, 
            endereco, 
            complemento, 
            bairro, 
            cep, 
            cidade, 
            uf
        )
        return response

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
        do = medicos_model.Medicos()
        response = do.EditarMedico(
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
        )
        return response

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
        do = pacientes_model.Pacientes()
        response = do.EditarPaciente(
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
        )
        return response