from backend.model import alergias_model
from backend.model import consultas_model
from backend.model import especialidade_medica_model
from backend.model import local_atendimento_model
from backend.model import medicos_model
from backend.model import pacientes_model
from typing import Any


class Search:

    @staticmethod
    def ListarAlergiasPorMatricula(matricula_sus) -> Any:
        do = alergias_model.Alergias()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarPacientesPorMatricula(matricula_sus) -> Any:
        do = pacientes_model.Pacientes()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarConsultasPorMatricula(matricula_sus) -> Any:
        do = consultas_model.Consultas()
        response = do.ListarPorMatricula(
            matricula_sus
        )
        return response

    @staticmethod
    def ListarAlergiasPorId(id) -> Any:
        do = alergias_model.Alergias()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarConsultasPorId(id) -> Any:
        do = consultas_model.Consultas()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarEspecialidadeMedicaPorId(id) -> Any:
        do = especialidade_medica_model.EspecialidadeMedica()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarLocalAtendimentoPorId(id) -> Any:
        do = local_atendimento_model.LocalAtendimento()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarMedicosPorId(id) -> Any:
        do = medicos_model.Medicos()
        response = do.ListarPorId(id)
        return response

    @staticmethod
    def ListarPacientesPorId(id) -> Any:
        do = pacientes_model.Pacientes()
        response = do.ListarPorId(id)
        return response


class Insert:

    @staticmethod
    def InserirAlergia(
        matricula_sus,
        descricao
    ) -> Any:
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
    ) -> Any:
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
    ) -> Any:
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
    ) -> Any:
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
    ) -> Any:
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
    ) -> Any:
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
