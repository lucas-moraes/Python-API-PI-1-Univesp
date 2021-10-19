from model import especialidade_medica_model

class Get:
    @staticmethod
    def ListarTodasEspecialidadesMedicas():
        do = especialidade_medica_model.EspecialidadeMedica()
        return do.ListarTodos()

