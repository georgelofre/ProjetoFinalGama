from flask import Flask, render_template
import mysql.connector
from ProjetoFinalGama.relatorio.dadosbd.dadosbd import configbanco,configteste
app = Flask(__name__)

def create_connection_database():
    if app.config['TESTING']: #por padrão TESTING=False
        return mysql.connector.connect(**configteste)
    else:
        return mysql.connector.connect(**configbanco)

mydb = create_connection_database()
teste = mydb.cursor()

@app.route('/index_relatorio')
def index_rel():
    return render_template('index_rel.html')

@app.route('/index_relatorio/maisvendido', methods=['GET'])
def maisvendido():
    teste.execute("select produto from relatorio01 where quantidade = (select max(quantidade) from relatorio01);")
    maisvend = teste.fetchone()
    return render_template('maisvendido.html', maisvendido=maisvend[0])

@app.route('/index_relatorio/osmaisvendidos', methods=['GET'])
def osmaisvendidos():
    teste.execute("select produto, quantidade from relatorio01 where quantidade > (select avg(quantidade) from relatorio01);")
    osmaisvend = teste.fetchall()
    return render_template('osmaisvendidos.html', osmaisvendidos=osmaisvend)

@app.route('/index_relatorio/totaldevendas', methods=['GET'])
def totalDeVendas():
    teste.execute("select sum(quantidade) from relatorio01;")
    quant = teste.fetchone()
    quantidade = int(quant[0])
    teste.execute("select sum(valor) from relatorio01;")
    arrec = teste.fetchone()
    arrecadado = f'{float(arrec[0]):.2f}'.replace(".", ",")
    dados = [quantidade, arrecadado]
    return render_template('totalvendas.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)