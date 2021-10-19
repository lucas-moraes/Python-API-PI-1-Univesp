from model import especialidade_medica_model

class Insert:
    @staticmethod
    def InserirEspecialidadeMedica(desc_especialidade):
        do = especialidade_medica_model.EspecialidadeMedica()
        do.InserirEspecialidade(desc_especialidade)
