import pytest
from ProjetoFinalGama.relatorio.app_mysql import create_app
import requests
from ProjetoFinalGama.relatorio.dadosbd.dadosdb import configteste


trunc = '''
Truncate Table relatorio01;
'''
insert = "INSERT INTO relatorioteste (id, produto, quantidade, valor) VALUES (%s, %s, %s, %s);"
val = ('1', 'Laranja', '4', '9.80')
'''
INSERT INTO `relatorioteste` (`id`, `produto`, `quantidade`, `valor`) VALUES ('1', 'Banana', '4', '9.80');
INSERT INTO `relatorioteste` (`id`, `produto`, `quantidade`, `valor`) VALUES ('2', 'Uva', '10', '15.20');
INSERT INTO `relatorioteste` (`id`, `produto`, `quantidade`, `valor`) VALUES ('3', 'Jambo', '7', '14.75');
INSERT INTO `relatorioteste` (`id`, `produto`, `quantidade`, `valor`) VALUES ('4', 'Tomate', '17', '23.60');
'''


@pytest.fixture
def client():
    app = create_app(configdados=configteste)
    return app

def test_index_rel_response(client):
    resposta = requests.get("http://127.0.0.1:5000/index_relatorio")
    print(resposta.text)
    assert resposta.status_code == 200

def test_maisvendido_response(client):
    resposta = requests.get("http://127.0.0.1:5000/index_relatorio/maisvendido")
    print(resposta.text)
    assert resposta.status_code == 200
    assert 'Limao' in resposta.text

def test_osmaisvendidos(client):
    resposta = requests.get("http://127.0.0.1:5000/index_relatorio/osmaisvendidos")
    assert resposta.status_code == 200
    assert 'Produto: Pessego, quantidade: 11 e valor: R$ 15.00' in resposta.text
    assert 'Produto: Limao, quantidade: 19 e valor: R$ 23.00' in resposta.text

def test_totalDeVendas(client):
    resposta = requests.get("http://127.0.0.1:5000/index_relatorio/totaldevendas")
    print(resposta.text)
    assert resposta.status_code == 200
    assert 'Foram vendidos 41 produtos, resultando no valor arrecadado de R$ ' in resposta.text



