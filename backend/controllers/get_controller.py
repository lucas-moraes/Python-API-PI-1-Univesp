from backend.model import alergias_model
from backend.model import consultas_model
from backend.model import especialidade_medica_model
from backend.model import local_atendimento_model
from backend.model import medicos_model
from backend.model import pacientes_model


class Get:

    @staticmethod
    def ListarTodasAlergias():
        do = alergias_model.Alergias()
        return do.ListarTodos()

    @staticmethod
    def ListarTodasConsultas():
        do = consultas_model.Consultas()
        return do.ListarTodos()

    @staticmethod
    def ListarTodasEspecialidadesMedicas():
        do = especialidade_medica_model.EspecialidadeMedica()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosLocalAtendimento():
        do = local_atendimento_model.LocalAtendimento()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosMedicos():
        do = medicos_model.Medicos()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosPacientes():
        do = pacientes_model.Pacientes()
        return do.ListarTodos()
