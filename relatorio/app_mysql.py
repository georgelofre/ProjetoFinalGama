import requests
from flask import Flask, render_template
import mysql.connector
from ProjetoFinalGama.relatorio.dadosbd.dadosbd import configbanco




app = Flask(__name__)

# exemplo para conectar no banco local:
#config = {'user': 'usuário',
#          'password': 'senha',
#          'host': 'localhost',
#          'database': 'nomedobanco'
#          }
# Substituir e Descomentar as duas linhas acima
# Comentar a linha 3: from config import config

#conexão com o banco mysql
#sugestão de preenchimento do banco: olhar arquivo tabeladb.txt
mydb = mysql.connector.connect(**configbanco)
teste = mydb.cursor()
teste.execute("SELECT * FROM testevendas.relatorio2")
tudo = teste.fetchall()
print(tudo)

@app.route('/index_relatorio')
def index_rel():
    return render_template('index_rel.html')

@app.route('/index_relatorio/maisvendido')
def maisvendido():
    teste.execute("select produto from relatorio where quantidade = (select max(quantidade) from relatorio);")
    maisvend = teste.fetchone()
    print(maisvend[0])
    return render_template('maisvendido.html', maisvendido=maisvend[0])

@app.route('/index_relatorio/osmaisvendidos')
def osmaisvendidos():
    teste.execute("select produto, quantidade from relatorio where quantidade > (select avg(quantidade) from relatorio);")
    osmaisvend = teste.fetchall()
    print(osmaisvend)
    return render_template('osmaisvendidos.html', osmaisvendidos=osmaisvend)

@app.route('/index_relatorio/totaldevendas')
def totalDeVendas():
    teste.execute("select sum(quantidade) from relatorio2;")
    quant = teste.fetchone()
    print(type(quant[0]))
    print(quant)
    quantidade = int(quant[0])
    print(quantidade)
    print(f'Qtde: {quantidade}')
    teste.execute("select sum(valor) from relatorio2;")
    arrec = teste.fetchone()
    print(arrec)
    arrecadado = f'{float(arrec[0]):.2f}'.replace(".", ",")
    print(f'Qtde: {arrecadado}')
    dados = [quantidade, arrecadado]
    return render_template('totalvendas.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)