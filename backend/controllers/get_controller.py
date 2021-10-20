from model import alergias_model, consultas_model, especialidade_medica_model

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


