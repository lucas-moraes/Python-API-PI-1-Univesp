from model import alergias_model, consultas_model, especialidade_medica_model

class Delete:

    @staticmethod
    def DeletarAlergia(id_alergia):
        do = alergias_model.Alergias()
        do.DeletarAlergia(id_alergia)

    @staticmethod
    def DeletarEspecialidadeMedica(id_especialidade_medica):
        do = especialidade_medica_model.EspecialidadeMedica()
        do.DeletarEspecialidade(id_especialidade_medica)

    @staticmethod
    def DeletarConsulta(id_consultas):
        do = consultas_model.Consultas()
        do.DeletarConsulta(id_consultas)