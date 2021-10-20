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

@app.put('/editar-especialidade-medica')
def EditarEspecialidadeMedica(id: int, edit: EspecialidadeMedica):
    edit_iten = update_controller.Update()
    edit_iten.EditarEspecialidadeMedica(id, edit.desc_especialidade)


#----------------------------------------#
#                                        #
#  Local Atendimento                     #
#                                        #
#----------------------------------------#

class LocalAtendimento(BaseModel):
    nome_local: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    uf: str

@app.get('/listar-local-atendimento')
def ListarLocalAtendimento():
    list = get_controller.Get()
    return list.ListarTodosLocalAtendimento()

@app.post('/inserir-local-atendimento')
def InserirLocalAtendimento(post: LocalAtendimento):
    iten = post_controller.Insert()
    iten.InserirLocalAtendiemnto(
        post.nome_local, 
        post.endereco, 
        post.complemento, 
        post.bairro, 
        post.cep, 
        post.cidade, 
        post.uf
    )

@app.put('/editar-local-atendimento')
def EditarLocalAtendimento(id: int, edit: LocalAtendimento):
    edit_iten = update_controller.Update()
    edit_iten.EditarConsulta(
        id, 
        edit.nome_local, 
        edit.endereco, 
        edit.complemento, 
        edit.bairro, 
        edit.cep, 
        edit.cidade, 
        edit.uf
    )

@app.delete('/deletar-local-atendimento/{id}')
def DeletarEspecialidadeMedica(id: int):
    iten = delete_controller.Delete()
    iten.DeletarLocalAtendimento(id)



#----------------------------------------#
#                                        #
#  Medicos                               #
#                                        #
#----------------------------------------#

class Medicos(BaseModel):
  crm: int
  nome: str
  sobrenome: str
  endereco: str
  complemento: str
  bairro: str
  cep: str
  cidade: str
  uf: str
  id_especialidade_medica: int

@app.get('/listar-medicos')
def ListarMedicos():
    list = get_controller.Get()
    return list.ListarTodosMedicos()

@app.post('/inserir-medico')
def InserirMedico(post: Medicos):
    iten = post_controller.Insert()
    iten.InserirMedico(
        post.crm,
        post.nome, 
        post.sobrenome, 
        post.endereco, 
        post.complemento, 
        post.bairro, 
        post.cep,
        post.cidade,
        post.uf,
        post.id_especialidade_medica
    )

@app.put('/editar-medico')
def EditarMedico(id: int, edit: Medicos):
    edit_iten = update_controller.Update()
    edit_iten.EditarMedico(
        id, 
        edit.crm,
        edit.nome, 
        edit.sobrenome, 
        edit.endereco, 
        edit.complemento, 
        edit.bairro, 
        edit.cep,
        edit.cidade,
        edit.uf,
        edit.id_especialidade_medica
    )

@app.delete('/deletar-medico/{id}')
def DeletarMedico(id: int):
    iten = delete_controller.Delete()
    iten.DeletarMedico(id)


#----------------------------------------#
#                                        #
#  Pacientes                             #
#                                        #
#----------------------------------------#

class Pacientes(BaseModel):
    matricula_sus: int
    data_registro: str
    tipo_sangue: str
    nome: str
    sobrenome: str
    data_nasc: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    uf: str

@app.get('/listar-pacientes')
def ListarPacientes():
    list = get_controller.Get()
    return list.ListarTodosPacientes()

@app.post('/inserir-paciente')
def InserirPaciente(post: Pacientes):
    iten = post_controller.Insert()
    iten.InserirPaciente(
        post.matricula_sus,
        post.data_registro,
        post.tipo_sangue,
        post.nome,
        post.sobrenome,
        post.data_nasc,
        post.endereco,
        post.complemento,
        post.bairro,
        post.cep,
        post.cidade,
        post.uf
    )

@app.put('/editar-paciente')
def EditarPaciente(id: int, edit: Pacientes):
    edit_iten = update_controller.Update()
    edit_iten.EditarPaciente(
        id, 
        edit.matricula_sus,
        edit.data_registro,
        edit.tipo_sangue,
        edit.nome,
        edit.sobrenome,
        edit.data_nasc,
        edit.endereco,
        edit.complemento,
        edit.bairro,
        edit.cep,
        edit.cidade,
        edit.uf
    )

@app.delete('/deletar-paciente/{id}')
def DeletarPaciente(id: int):
    iten = delete_controller.Delete()
    iten.DeletarPaciente(id)


