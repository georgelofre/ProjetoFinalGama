from flask import Flask, render_template
import mysql.connector as sql
from ProjetoFinalGama.relatorio.dadosbd.dadosdb import configteste, configreal

def create_app(configdados):

    # create a minimal app
    app = Flask(__name__)

    def create_connection_database():
        return sql.connect(**configdados)

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

    @app.route('/index_relatorio/rankprodutos', methods=['GET'])
    def rank_de_produtos():
        mydb = create_connection_database()
        mycursor = mydb.cursor()
        mycursor.execute("select produto, quantidade, valor from relatorio01 order by quantidade ASC;")
        rank = mycursor.fetchall()
        mydb.close()
        return render_template('rankprodutos.html', rank=rank, len=len(rank))

    @app.route('/index_relatorio/limpartabela', methods=['GET'])
    def limpar_tabela():
        mydb = create_connection_database()
        mycursor = mydb.cursor()
        mycursor.execute("TRUNCATE TABLE relatorio01;")
        mydb.commit()
        mydb.close()
        return render_template('limpartabela.html')

    @app.route('/index_relatorio/consultar', methods=['GET'])
    def consultar_vendas():
        mydb = create_connection_database()
        mycursor = mydb.cursor()
        mycursor.execute("select produto from relatorio01;")
        produtos = mycursor.fetchall()
        mycursor.execute("select avg(quantidade) from relatorio01;")
        quantidademedia = mycursor.fetchone()
        mycursor.execute("select avg(valor) from relatorio01;")
        valormedio = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        return render_template('consultarvendas.html', produtos=produtos, qtdmedia=quantidademedia, valmedio=valormedio)

    return app

