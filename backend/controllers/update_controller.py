from model import alergias_model, consultas_model

class Update:

    @staticmethod
    def EditarAlergia(id_alergias, descricao):
        do = alergias_model.Alergias()
        do.EditarAlergia(id_alergias, descricao)

    @staticmethod
    def EditarConsulta(d_consultas, matricula_sus, id_especialidade_medica, data_hora_marca, id_medico, id_local_atendimento, compareceu):
        do = consultas_model.Consultas()
        do.EditarConsulta(d_consultas, matricula_sus, id_especialidade_medica, data_hora_marca, id_medico, id_local_atendimento, compareceu)