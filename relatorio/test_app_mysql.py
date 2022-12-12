import pytest
import requests
from ProjetoFinalGama.relatorio.app_mysql import app

@pytest.fixture()
def client():
    return app.test_client()

def test_index_rel_response(client):
    resposta = client.get("http://127.0.0.1:5000/index_relatorio")
    assert resposta.status_code == 200

