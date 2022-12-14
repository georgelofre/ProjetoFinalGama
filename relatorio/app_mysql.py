from flask import Flask, render_template
import mysql.connector as sql
from ProjetoFinalGama.relatorio.dadosbd.dadossbd import configbanco, configteste, testando
app = Flask(__name__)

config = {'user': 'root',
          'password': 'Ml_339427',
          'host': 'localhost',
          'database': 'new_relatorio'
          }

configteste = {'user': 'root',
          'password': 'Ml_339427',
          'host': 'localhost',
          'database': 'teste_relatorio'
          }

def create_connection_database():
    if testando == True:
        return sql.connect(**config)
    else:
        return sql.connect(**configteste)


mydb = create_connection_database()
teste = mydb.cursor()

@app.route('/index_relatorio')
def index_rel():
    return render_template('index_rel.html')

@app.route('/index_relatorio/maisvendido', methods=['GET'])
def maisvendido():
    teste.execute("select produto, quantidade, valor from relatorio01 where quantidade = (select max(quantidade) from relatorio01);")
    maisvend = teste.fetchone()
    return render_template('maisvendido.html', maisvendido=maisvend)

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

@app.route('/index_relatorio/rankprodutos', methods=['GET'])
def rankprodutos():
    teste.execute("select produto, quantidade from relatorio01 where quantidade > (select avg(quantidade) from relatorio01);")
    osmaisvend = teste.fetchall()
    return render_template('osmaisvendidos.html', osmaisvendidos=osmaisvend)

@app.route('/index_relatorio/limpar', methods=['GET'])
def limpar():
    teste.execute("delete from relatorio01 ")
    mydb.commit()
    return render_template('osmaisvendidos.html')

@app.route('/index_relatorio/consultar', methods=['GET'])
def consultar():
    teste.execute("select produto, quantidade from relatorio01;")
    osmaisvend = teste.fetchall()
    return render_template('osmaisvendidos.html', osmaisvendidos=osmaisvend)


if __name__ == '__main__':
    app.run(debug=True)
