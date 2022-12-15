import pytest
from mongo_app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_cadastrar(client):
    resultado = client.get('/cadastrar/?nome=teste&preco=2&descricao=descriteste')
    assert resultado.json == {'nome: teste', 'preco: 2', 'descricao: descriteste'}

def test_cadastrar_status(client):
    resultado = client.get('/cadastrar/?nome=teste&preco=2&descricao=descriteste')
    assert resultado.status_code == 200

def test_consultar(client):
    resultado = client.get('/consultar/')
    assert resultado.json == {'nome: teste', 'preco: 2', 'descricao: descriteste'}

def test_consultar_status(client):
    resultado = client.get('/consultar/')
    assert resultado.status_code == 200

def test_deletar(client):
    resultado = client.get()
    assert resultado.json == {}

def test_deletar_status(client):
    resultado = client.get()
    assert resultado.status_code == 200

def test_atualizar(client):
    resultado = client.get()
    assert resultado.json == {}

def test_atualizar_status(client):
    resultado = client.get()
    assert resultado.status_code == 200