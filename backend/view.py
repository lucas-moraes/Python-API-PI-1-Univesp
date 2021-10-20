from fastapi import FastAPI
from controllers import get_controller, post_controller, delete_controller, update_controller
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
    return {"home": "It's running !"}


#----------------------------------------#
#                                        #
#  Alergias                              #
#                                        #
#----------------------------------------#

class Alergias(BaseModel):
    id_alergias: int
    matricula_sus: int
    descricao: str

@app.get('/listar-alergias')
def ListarAlergias():
    list = get_controller.Get()
    return list.ListarTodasAlergias()

@app.post('/inserir-alergia')
def InserirAlergia(inserir: Alergias):
    iten = post_controller.Insert()
    iten.InserirAlergia(inserir.matricula_sus, inserir.descricao)

@app.put('/editar-alergia')
def EditarAlergia(id: int, desc: str):
    edit_iten = update_controller.Update()
    edit_iten.EditarAlergia(id, desc)

@app.delete('/deletar-alergia/{id}')
def DeletarAlergia(id: int):
    iten = delete_controller.Delete()
    iten.DeletarAlergia(id)


#----------------------------------------#
#                                        #
#  Consultas                             #
#                                        #
#----------------------------------------#

class Consultas(BaseModel):
  matricula_sus: int
  id_especialidade_medica: int
  data_hora_marcada: str #YYYY-MM-DD hh:mm:ss
  id_medico: int
  id_local_atendimento: int
  compareceu: bool

@app.get('/listar-consultas')
def ListarConsultas():
    list = get_controller.Get()
    return list.ListarTodasConsultas()

@app.post('/inserir-consulta')
def InserirConsulta(inserir: Consultas):
    iten = post_controller.Insert()
    iten.InserirConsulta(inserir.matricula_sus, inserir.id_especialidade_medica, inserir.data_hora_marcada, inserir.id_medico, inserir.id_local_atendimento, inserir.compareceu)

@app.put('/editar-consulta')
def EditarConsulta(id: int, edit: Consultas):
    edit_iten = update_controller.Update()
    edit_iten.EditarConsulta(id, edit.matricula_sus, edit.id_especialidade_medica, edit.data_hora_marcada, edit.id_medico, edit.id_local_atendimento, edit.compareceu)

@app.delete('/deletar-consulta/{id}')
def DeletarConsulta(id: int):
    iten = delete_controller.Delete()
    iten.DeletarConsulta(id)

#----------------------------------------#
#                                        #
#  Especialidade Medicas                 #
#                                        #
#----------------------------------------#

class EspecialidadeMedica(BaseModel):
    desc_especialidade: str

@app.get('/listar-especialidades-medicas')
def ListarEspecialidadesMedicas():
    list = get_controller.Get()
    return list.ListarTodasEspecialidadesMedicas()

@app.post('/inserir-especialidade-medica')
def InserirEspecialidadMedica(post: EspecialidadeMedica):
    iten = post_controller.Insert()
    iten.InserirEspecialidadeMedica(post.desc_especialidade)
    return True

@app.delete('/deletar-especialidade-medica/{id}')
def DeletarEspecialidadeMedica(id: int):
    iten = delete_controller.Delete()
    iten.DeletarEspecialidadeMedica(id)

