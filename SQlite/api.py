from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql

app = Flask(__name__)
banco = 'organicos.bd'

# Função
def abrir_conexao(banco):
    conexao = sql.connect(banco)
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

# Comandos consulta de itens e alteração de quantidade
select_todos = "SELECT * FROM nome_tabela;"
select_id = "SELECT * FROM nome_tabela WHERE nome like ?"
update = "UPDATE nome_tabela SET quantidade =:quantidade WHERE quantidade like :quantidade  "

# alterar quantidade
@app.route('/update/<quantidade>')
def update_quantidade(quantidade):
    consulta = read(quantidade)
    if consulta: 
        id=request.args.to_dict() 
        if id: 
            conexao, cursor = abrir_conexao(banco)
            cursor.execute(update, quantidade)
            fechar_conexao(conexao)
            return id
        else: 
            return render_template('alterar_quantidade.html', nome_tabela=consulta[0])
    else:
        return {'error': 'mensagem de erro'}

# consulta de produtos 
@app.route('/read')
def read():
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(select_todos).fetchall()
    fechar_conexao(conexao)
    return resultado        


if __name__ == "__main__":
    app.run(debug=True)    