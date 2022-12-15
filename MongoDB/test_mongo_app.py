import pytest
from mongo_app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_cadastrar(client):
    resultado = client.get('/cadastrar')
    assert len (resultado.history) == 1
    assert resultado.request.path == '/cadastrado.html'
    #assert resultado.json == {'nome: teste', 'preco: 2', 'descricao: descriteste'}

def test_cadastrar_status(client):
    resultado = client.get('/cadastrar')
    assert resultado.status_code == 302

def test_consultar(client):
    resultado = client.get('/consultar')
    assert len (resultado.history) == 1
    assert resultado.request.path == '../templates/consultado.html'    

def test_consultar_status(client):
    resultado = client.get('/consultar')
    assert resultado.status_code == 320

def test_atualizar(client):
    resultado = client.get('/atualizar')
    assert len (resultado.history) == 1
    assert resultado.request.path == '/atualizado.html'
    #assert resultado.json == {'nome: teste', 'preco: 3', 'descricao: outradescriteste'}

def test_atualizar_status(client):
    resultado = client.get('/atualizar')
    assert resultado.status_code == 320

def test_deletar(client):
    resultado = client.get('/deletar')
    assert len (resultado.history) == 1
    assert resultado.request.path == '/deletado.html'

def test_deletar_status(client):
    resultado = client.get('/deletar')
    assert resultado.status_code == 320