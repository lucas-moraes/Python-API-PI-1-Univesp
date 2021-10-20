from model import alergias_model, consultas_model, especialidade_medica_model

class Insert:

    @staticmethod
    def InserirAlergia(matricula_sus, descricao):
        do = alergias_model.Alergias()
        do.InserirAlergia(matricula_sus, descricao)


    @staticmethod
    def InserirEspecialidadeMedica(desc_especialidade):
        do = especialidade_medica_model.EspecialidadeMedica()
        do.InserirEspecialidade(desc_especialidade)


    @staticmethod
    def InserirConsulta(matricula_sus, id_especialidade_medica, data_hora_marca, id_medico, id_local_atendimento, compareceu):
        do = consultas_model.Consultas()
        do.InserirConsulta(matricula_sus, id_especialidade_medica, data_hora_marca, id_medico, id_local_atendimento, compareceu)