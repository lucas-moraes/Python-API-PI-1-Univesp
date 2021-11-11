from backend.model import alergias_model
from backend.model import consultas_model
from backend.model import especialidade_medica_model
from backend.model import local_atendimento_model
from backend.model import medicos_model
from backend.model import pacientes_model


class Delete:

    @staticmethod
    def DeletarAlergia(id_alergia):
        do = alergias_model.Alergias()
        response = do.DeletarAlergia(id_alergia)
        return response

    @staticmethod
    def DeletarConsulta(id_consultas):
        do = consultas_model.Consultas()
        response = do.DeletarConsulta(id_consultas)
        return response

    @staticmethod
    def DeletarEspecialidadeMedica(id_especialidade_medica):
        do = especialidade_medica_model.EspecialidadeMedica()
        response = do.DeletarEspecialidade(id_especialidade_medica)
        return response

    @staticmethod
    def DeletarLocalAtendimento(id_local_atendimento):
        do = local_atendimento_model.LocalAtendimento()
        response = do.DeletarLocalAtendimento(id_local_atendimento)
        return response

    @staticmethod
    def DeletarMedico(id_medico):
        do = medicos_model.Medicos()
        response = do.DeletarMedico(id_medico)
        return response

    @staticmethod
    def DeletarPaciente(id_paciente):
        do = pacientes_model.Pacientes()
        response = do.DeletarPaciente(id_paciente)
        return response
