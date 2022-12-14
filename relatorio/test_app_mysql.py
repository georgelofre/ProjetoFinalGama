import pytest
from ProjetoFinalGama.relatorio.app_mysql import app, create_connection_database

testanto = True

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
    return app.test_client()


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
    assert 'Uva' in resposta.text

def test_totalDeVendas(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio/totaldevendas")
    assert resposta.status_code == 200
    assert '38' in resposta.text
    assert '63,35' in resposta.text



