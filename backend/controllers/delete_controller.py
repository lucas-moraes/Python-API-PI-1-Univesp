from backend.model import alergias_model
from backend.model import consultas_model
from backend.model import especialidade_medica_model
from backend.model import local_atendimento_model
from backend.model import medicos_model
from backend.model import pacientes_model


class Delete:

    @staticmethod
    def DeletarAlergia(id_alergia) -> bool:
        do = alergias_model.Alergias()
        response = do.DeletarAlergia(id_alergia)
        return response

    @staticmethod
    def DeletarConsulta(id_consultas) -> bool:
        do = consultas_model.Consultas()
        response = do.DeletarConsulta(id_consultas)
        return response

    @staticmethod
    def DeletarEspecialidadeMedica(id_especialidade_medica) -> bool:
        do = especialidade_medica_model.EspecialidadeMedica()
        response = do.DeletarEspecialidade(id_especialidade_medica)
        return response

    @staticmethod
    def DeletarLocalAtendimento(id_local_atendimento) -> bool:
        do = local_atendimento_model.LocalAtendimento()
        response = do.DeletarLocalAtendimento(id_local_atendimento)
        return response

    @staticmethod
    def DeletarMedico(id_medico) -> bool:
        do = medicos_model.Medicos()
        response = do.DeletarMedico(id_medico)
        return response

    @staticmethod
    def DeletarPaciente(id_paciente) -> bool:
        do = pacientes_model.Pacientes()
        response = do.DeletarPaciente(id_paciente)
        return response
