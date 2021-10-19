from fastapi import FastAPI
from controllers import get_controller, insert_controller, delete_controller
from pydantic import BaseModel

app = FastAPI()

class EspecialidadeMedica(BaseModel):
    desc_especialidade: str

@app.get('/')
def root():
    return {"home": "It's running !"}

@app.get('/listar-especialidades-Medicas')
def ListarEspecialidadesMedicas():
    list = get_controller.Get()
    return list.ListarTodasEspecialidadesMedicas()

@app.post('/inserir-especialidade-Medica')
def InserirEspecialidadMedica(post: EspecialidadeMedica):
    iten = insert_controller.Insert()
    iten.InserirEspecialidadeMedica(post.desc_especialidade)
    return True

@app.delete('/deletar-especialidade-medica/{id}')
def DeletarEspecialidadeMedica(id: int):
    iten = delete_controller.Delete()
    iten.DeletarEspecialidadeMedica(id)