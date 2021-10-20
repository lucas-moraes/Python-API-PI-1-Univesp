from model import alergias_model
from model import consultas_model
from model import especialidade_medica_model
from model import local_atendimento_model
from model import medicos_model
from model import pacientes_model


class Delete:

    @staticmethod
    def DeletarAlergia(id_alergia):
        do = alergias_model.Alergias()
        do.DeletarAlergia(id_alergia)

    @staticmethod
    def DeletarConsulta(id_consultas):
        do = consultas_model.Consultas()
        do.DeletarConsulta(id_consultas)

    @staticmethod
    def DeletarEspecialidadeMedica(id_especialidade_medica):
        do = especialidade_medica_model.EspecialidadeMedica()
        do.DeletarEspecialidade(id_especialidade_medica)

    @staticmethod
    def DeletarLocalAtendimento(id_local_atendimento):
        do = local_atendimento_model.LocalAtendimento()
        do.DeletarLocalAtendimento(id_local_atendimento)

    @staticmethod
    def DeletarMedico(id_medico):
        do = medicos_model.Medicos()
        do.DeletarMedico(id_medico)

    @staticmethod
    def DeletarPaciente(id_paciente):
        do = pacientes_model.Pacientes()
        do.DeletarPaciente(id_paciente)