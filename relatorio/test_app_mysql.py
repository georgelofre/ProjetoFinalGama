import pytest
from ProjetoFinalGama.relatorio.app_mysql import app

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

@pytest.fixture()
def client():
    testing_client = app.test_client()
    return testing_client



def test_index_rel_response(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio")
    assert resposta.status_code == 200

def test_maisvendido_response(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio/maisvendido")
    assert resposta.status_code == 200
    assert 'Tomate' in resposta.text

def test_osmaisvendidos(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio/osmaisvendidos")
    assert resposta.status_code == 200
    banco_teste_01 = 'Produto: Pessego, quantidade: 10 e valor: R$ 15.20'
    banco_teste_02 = 'Produto: Limao, quantidade: 17 e valor: R$ 23.60'
    assert banco_teste_01, banco_teste_02 in resposta.text

def test_totalDeVendas(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio/totaldevendas")
    print(resposta.text)
    assert resposta.status_code == 200
    banco_teste_03 = 'Foram vendidos 41 produtos, resultando no valor arrecadado de R$ '
    assert banco_teste_03 in resposta.text



