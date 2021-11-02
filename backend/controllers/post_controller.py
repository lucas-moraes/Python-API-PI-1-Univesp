from os import stat
from model import alergias_model
from model import consultas_model
from model import especialidade_medica_model
from model import local_atendimento_model
from model import medicos_model
from model import pacientes_model


class Search:

    @staticmethod
    def ListarAlergiasPorMatricula(matricula_sus):
        do = alergias_model.Alergias()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarPacientesPorMatricula(matricula_sus):
        do = pacientes_model.Pacientes()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarConsultasPorMatricula(matricula_sus):
        do = consultas_model.Consultas()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarAlergiasPorId(id):
        do = alergias_model.Alergias()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarConsultasPorId(id):
        do = consultas_model.Consultas()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarEspecialidadeMedicaPorId(id):
        do = especialidade_medica_model.EspecialidadeMedica()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarLocalAtendimentoPorId(id):
        do = local_atendimento_model.LocalAtendimento()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarMedicosPorId(id):
        do = medicos_model.Medicos()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarPacientesPorId(id):
        do = pacientes_model.Pacientes()
        response = do.ListarPorId(id)
        return response


class Insert:

    @staticmethod
    def InserirAlergia(
        matricula_sus,
        descricao
    ):
        do = alergias_model.Alergias()
        response = do.InserirAlergia(
            matricula_sus,
            descricao
        )
        return response

    @staticmethod
    def InserirConsulta(
        matricula_sus,
        id_especialidade_medica,
        data_hora_marca, id_medico,
        id_local_atendimento, compareceu
    ):
        do = consultas_model.Consultas()
        response = do.InserirConsulta(
            matricula_sus,
            id_especialidade_medica,
            data_hora_marca,
            id_medico,
            id_local_atendimento,
            compareceu
        )
        return response

    @staticmethod
    def InserirEspecialidadeMedica(
        desc_especialidade
    ):
        do = especialidade_medica_model.EspecialidadeMedica()
        response = do.InserirEspecialidade(
            desc_especialidade
        )
        return response

    @staticmethod
    def InserirLocalAtendiemnto(
        nome_local,
        endereco,
        complemento,
        bairro,
        cep,
        cidade,
        uf
    ):
        do = local_atendimento_model.LocalAtendimento()
        response = do.InserirLocalAtendimento(
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
        do = medicos_model.Medicos()
        response = do.InserirMedico(
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
        do = pacientes_model.Pacientes()
        response = do.InserirPaciente(
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
