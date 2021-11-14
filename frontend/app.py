from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def Consulta():
    return render_template('consulta.html', pagename="consulta")


@app.route('/listas')
def Listas():

    lista_pacientes = requests.get(
        url='http://127.0.0.1:8000/listar-pacientes')
    listagem_pacientes_json = lista_pacientes.json()
    pacientes = []
    for iten in listagem_pacientes_json:
        pacientes.append(iten)

    lista_consultas = requests.get(
        url='http://127.0.0.1:8000/listar-consultas')
    listagem_consultas_json = lista_consultas.json()
    consultas = []
    for iten in listagem_consultas_json:
        consultas.append(iten)

    lista_medicos = requests.get(url='http://127.0.0.1:8000/listar-medicos')
    listagem_medicos_json = lista_medicos.json()
    medicos = []
    for iten in listagem_medicos_json:
        medicos.append(iten)

    lista_especialidades_medicas = requests.get(
        url='http://127.0.0.1:8000/listar-especialidades-medicas')
    listagem_especialidades_medicas_json = lista_especialidades_medicas.json()
    especialidades_medicas = []
    for iten in listagem_especialidades_medicas_json:
        especialidades_medicas.append(iten)

    lista_local_atendimento = requests.get(
        url='http://127.0.0.1:8000/listar-local-atendimento')
    listagem_local_atendimento_json = lista_local_atendimento.json()
    local_atendimento = []
    for iten in listagem_local_atendimento_json:
        local_atendimento.append(iten)

    return render_template('listas.html', pacientes=pacientes, consultas=consultas, medicos=medicos, especialidades_medicas=especialidades_medicas, local_atendimento=local_atendimento)
