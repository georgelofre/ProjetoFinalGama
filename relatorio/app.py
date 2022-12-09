from flask import Flask
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

teste.execute("SELECT * FROM relatorio")

resultado = teste.fetchall()

@app.route('/index_relatorio')
def index_rel():
    return f'{resultado}'

if __name__ == '__main__':
    app.run(debug=True)