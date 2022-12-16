from api import app
#from unittest import mock
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_route_home(client):
    resultado = client.get('/')
    assert resultado.status_code == 200

#Testes de retorno para a rota adicionar
def test_route_add_produto_should_return_ok(client):
    resultado = client.post('/adiciona', json = {
      "nome": "agua",
      "quantidade": 2,
      "preco": 4.0
    })
    assert resultado.status_code == 201

def test_route_add_produto_should_return_erro(client):
    resultado = client.post('/adiciona', json = {
 })
    assert resultado.json == {"erro": "Esperava receber uma solicitação"}

#Testes de retorno para a rota de consulta
def test_should_return_status_200_when_prod_is_registered(client):
    resultado = client.get('consulta/agua')
    assert resultado.status_code == 200

def test_should_return_json_when_prod_is_not_registered(client):
    resultado = client.get('consulta/uva')
    assert resultado.json == {"erro":"Produto não registrado"}

def test_should_return_status_200(client):
    resultado = client.get('/consulta_tudo')
    assert resultado.status_code == 200

#Testes de retorno para a rota deletar
def test_should_return_status_200_when_prod_name_is_del(client):
    resultado = client.delete('/deleta/agua')
    assert resultado.status_code == 200

def test_should_return_json_when_prod_name_not_found(client):
    resultado = client.delete('/deleta/manga')
    assert resultado.json == {"erro": "Produto não encontrado"}

def test_should_return_JASON_when_all_prod_are_deleted(client):
    resultado = client.delete('/deleta_tudo')
    assert resultado.json == {"mensagem":"Todos os produtos foram removidos"}