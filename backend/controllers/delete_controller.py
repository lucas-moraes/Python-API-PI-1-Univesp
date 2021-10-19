from model import especialidade_medica_model

class Delete:
    @staticmethod
    def DeletarEspecialidadeMedica(id_especialidade_medica):
        do = especialidade_medica_model.EspecialidadeMedica()
        do.DeletarEspecialidade(id_especialidade_medica)