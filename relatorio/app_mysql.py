from flask import Flask, render_template
import mysql.connector as sql
from ProjetoFinalGama.relatorio.dadosbd.dadosbd import config, configteste

app = Flask(__name__)

def create_connection_database():
    if app.config['TESTING']:
        return sql.connect(**configteste)
    else:
        return sql.connect(**config)


@app.route('/index_relatorio')
def index_rel():
    return render_template('index_rel.html')

@app.route('/index_relatorio/maisvendido', methods=['GET'])
def maisvendido():
    mydb = create_connection_database()
    mycursor = mydb.cursor()
    mycursor.execute("select produto, quantidade, valor from relatorio01 where quantidade = (select max(quantidade) from relatorio01);")
    maisvend = mycursor.fetchone()
    mydb.close()
    return render_template('maisvendido.html', maisvendido=maisvend)

@app.route('/index_relatorio/osmaisvendidos', methods=['GET'])
def osmaisvendidos():
    mydb = create_connection_database()
    mycursor = mydb.cursor()
    mycursor.execute("select produto, quantidade, valor from relatorio01 where quantidade > (select avg(quantidade) from relatorio01);")
    osmaisvend = mycursor.fetchall()
    mydb.close()
    return render_template('osmaisvendidos.html', osmaisvendidos=osmaisvend)

@app.route('/index_relatorio/totaldevendas', methods=['GET'])
def totalDeVendas():
    mydb = create_connection_database()
    mycursor = mydb.cursor()
    mycursor.execute("select sum(quantidade) from relatorio01;")
    quantidade = mycursor.fetchone()
    mycursor.execute("select sum(valor) from relatorio01;")
    arrecadado = mycursor.fetchone()
    mydb.close()
    return render_template('totalvendas.html', quantidade=quantidade,
                           arrecadado=arrecadado)


if __name__ == '__main__':
    app.run(debug=True)
