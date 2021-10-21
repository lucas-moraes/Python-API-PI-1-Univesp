from fastapi import FastAPI
from controllers import get_controller
from controllers import post_controller
from controllers import delete_controller
from controllers import update_controller
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
    matricula_sus: int
    descricao: str

@app.get('/listar-alergias')
def ListarAlergias():
    try:
        do = get_controller.Get()
        lista = do.ListarTodasAlergias()
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"response":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-alergia')
def InserirAlergia(inserir: Alergias):
    try:
        do = post_controller.Insert()
        response = do.InserirAlergia(
            inserir.matricula_sus, 
            inserir.descricao
        )
        if response is False:
            return {"response": "Alergia depende do Paciente"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-alergia')
def EditarAlergia(id: int, desc: str):
    try:
        do = update_controller.Update()
        response = do.EditarAlergia(id, desc)
        if response is False:
           return {"response":"Edição não realizada"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.delete('/deletar-alergia/{id}')
def DeletarAlergia(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarAlergia(id)
        if response is False:
           return {"response":"Exclusão não realizada"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}


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
    try:
        do = get_controller.Get()
        lista = do.ListarTodasConsultas()    
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"atenção":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-consulta')
def InserirConsulta(inserir: Consultas):
    try:
        iten = post_controller.Insert()
        response = iten.InserirConsulta(
            inserir.matricula_sus, 
            inserir.id_especialidade_medica, 
            inserir.data_hora_marcada, 
            inserir.id_medico, 
            inserir.id_local_atendimento, 
            inserir.compareceu
        )
        if response is False:
            return {"response": "Consulta depende do Paciente, Local de atendimento, medicos e especialidade médica"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-consulta')
def EditarConsulta(id: int, edit: Consultas):
    try:
        do = update_controller.Update()
        response = do.EditarConsulta(
            id, 
            edit.matricula_sus, 
            edit.id_especialidade_medica, 
            edit.data_hora_marcada, 
            edit.id_medico, 
            edit.id_local_atendimento, 
            edit.compareceu
        )
        if response is False:
           return {"response":"Edição não realizada"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.delete('/deletar-consulta/{id}')
def DeletarConsulta(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarConsulta(id)
        if response is False:
           return {"response":"Edição não realizada"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}
        

#----------------------------------------#
#                                        #
#  Especialidade Medicas                 #
#                                        #
#----------------------------------------#

class EspecialidadeMedica(BaseModel):
    desc_especialidade: str

@app.get('/listar-especialidades-medicas')
def ListarEspecialidadesMedicas():
    try:
        do = get_controller.Get()
        lista = do.ListarTodasEspecialidadesMedicas()
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"atenção":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-especialidade-medica')
def InserirEspecialidadMedica(post: EspecialidadeMedica):
    try:
        do = post_controller.Insert()
        response = do.InserirEspecialidadeMedica(
            post.desc_especialidade
        )
        if response is False:
            return {"response": "Erro Interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-especialidade-medica')
def EditarEspecialidadeMedica(id: int, edit: EspecialidadeMedica):
    try:
        do = update_controller.Update()
        response = do.EditarEspecialidadeMedica(id, edit.desc_especialidade)
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.delete('/deletar-especialidade-medica/{id}')
def DeletarEspecialidadeMedica(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarEspecialidadeMedica(id)
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}


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
    try:
        do = get_controller.Get()
        lista = do.ListarTodosLocalAtendimento()
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"atenção":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-local-atendimento')
def InserirLocalAtendimento(post: LocalAtendimento):
    try:
        do = post_controller.Insert()
        response = do.InserirLocalAtendiemnto(
            post.nome_local, 
            post.endereco, 
            post.complemento, 
            post.bairro, 
            post.cep, 
            post.cidade, 
            post.uf
        )
        if response is False:
            return {"response": "Erro Interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-local-atendimento')
def EditarLocalAtendimento(id: int, edit: LocalAtendimento):
    try:
        do = update_controller.Update()
        response = do.EditarConsulta(
            id, 
            edit.nome_local, 
            edit.endereco, 
            edit.complemento, 
            edit.bairro, 
            edit.cep, 
            edit.cidade, 
            edit.uf
        )
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.delete('/deletar-local-atendimento/{id}')
def DeletarEspecialidadeMedica(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarLocalAtendimento(id)
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

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
    try:
        do = get_controller.Get()
        lista = do.ListarTodosMedicos()
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"atenção":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-medico')
def InserirMedico(post: Medicos):
    try:
        do = post_controller.Insert()
        response = do.InserirMedico(
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
        if response is False:
            return {"response": "Erro Interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-medico')
def EditarMedico(id: int, edit: Medicos):
    try:
        do = update_controller.Update()
        response = do.EditarMedico(
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
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.delete('/deletar-medico/{id}')
def DeletarMedico(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarMedico(id)
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

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
    try:
        do = get_controller.Get()
        lista = do.ListarTodosPacientes()
        if lista is False:
            return {"response": "Erro na consulta"}
        elif (lista is None):
            return {"atenção":"Lista vazia"}        
        return lista
    except:
        return {"response": "Erro na execução"}

@app.post('/inserir-paciente')
def InserirPaciente(post: Pacientes):
    try:
        do = post_controller.Insert()
        response = do.InserirPaciente(
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
        if response is False:
            return {"response": "Erro Interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}

@app.put('/editar-paciente')
def EditarPaciente(id: int, edit: Pacientes):
    try:
        do = update_controller.Update()
        response = do.EditarPaciente(
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
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}        

@app.delete('/deletar-paciente/{id}')
def DeletarPaciente(id: int):
    try:
        do = delete_controller.Delete()
        response = do.DeletarPaciente(id)
        if response is False:
           return {"response":"Erro interno"}
        return {"response": "Executado com sucesso!"}
    except:
        return {"response": "Erro na execução"}
