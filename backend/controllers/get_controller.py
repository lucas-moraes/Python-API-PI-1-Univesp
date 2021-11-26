from backend.model import alergias_model
from backend.model import consultas_model
from backend.model import especialidade_medica_model
from backend.model import local_atendimento_model
from backend.model import medicos_model
from backend.model import pacientes_model
from typing import Any


class Get:

    @staticmethod
    def ListarTodasAlergias() -> Any:
        do = alergias_model.Alergias()
        return do.ListarTodos()

    @staticmethod
    def ListarTodasConsultas() -> Any:
        do = consultas_model.Consultas()
        return do.ListarTodos()

    @staticmethod
    def ListarTodasEspecialidadesMedicas() -> Any:
        do = especialidade_medica_model.EspecialidadeMedica()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosLocalAtendimento() -> Any:
        do = local_atendimento_model.LocalAtendimento()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosMedicos() -> Any:
        do = medicos_model.Medicos()
        return do.ListarTodos()

    @staticmethod
    def ListarTodosPacientes() -> Any:
        do = pacientes_model.Pacientes()
        return do.ListarTodos()
