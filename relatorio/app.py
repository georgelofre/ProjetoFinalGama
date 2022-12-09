from flask import Flask, render_template, url_for
import mysql.connector
from config import config


app = Flask(__name__)
# exemplo para conectar no banco local:
# config = {'user': 'seu usuario','password': 'senha',
#           'host':'localhost','database':'nome do banco'}
# Substituir e Descomentar as duas linhas acima
# Comentar a linha 3: from config import config
mydb = mysql.connector.connect(**config)
teste = mydb.cursor()
teste.execute("SELECT * FROM testevendas.relatorio")
tudo = teste.fetchall()
print(tudo)



@app.route('/index_relatorio')
def index_rel():
    return render_template('index_rel.html')

@app.route('/index_relatorio/maisvendido')
def maisvendido():
    teste.execute("SELECT produto FROM testevendas.relatorio wEHERE")
    maisvend = teste.fetchall()
    print(maisvend)
    return render_template('maisvendido.html', maisvendido=maisvend)

if __name__ == '__main__':
    app.run(debug=True)