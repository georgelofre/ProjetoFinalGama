from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql

app = Flask(__name__)
banco = 'carrinho.db'

#funções (conexão com o banco)
def abrir_conn(banco):
    conn = sql.connect(banco)
    cursor = conn.cursor()
    return conn, cursor

def fechar_conn(conn):
    conn.commit()
    conn.close()

#comandos 
#criar tabela

tabela_carrinho = """CREATE TABLE  IF NOT EXISTS tabela_carrinho(
    id INT AUTO_INCREMENT, 
    nome TEXT,
    quantidade INT,
    preco FLOAT
);"""
inserir_prod = "INSERT INTO tabela_carrinho VALUES (null, :nome, :quantidade, :preco);"
deletar_prod = "DELETE FROM tabela_carrinho WHERE nome = ?;"
deletar_tudo = "DELETE FROM tabela_carrinho;"
consultar_tudo = "SELECT * FROM tabela_carrinho;"
consultar_nome = "SELECT * FROM tabela_carrinho WHERE nome = ?;"
update = "UPDATE tabela_carrinho SET quantidade =:quantidade WHERE quantidade like :quantidade  "

#criando tabela
conexao, cursor = abrir_conn(banco)
cursor.execute(tabela_carrinho)
fechar_conn(conexao)

#api
@app.get('/') # teste de rota
def home(): 
    return "Organico's", 200

#adicionando produtos
@app.route('/adiciona', methods=['POST'])
def adicionar_produto_carrinho():
    produto = request.json
    if produto:
        conexao, cursor = abrir_conn(banco)
        #print(type(conexao), type(cursor))
        cursor.execute(inserir_prod, produto)
        fechar_conn(conexao)
        return {"mensagem":"produto adicionado com sucesso"}, 201
    else:
        return {"erro": "Esperava receber uma solicitação"} , 400

#deletando produtos
@app.route('/deleta/<nome>', methods=['DELETE'])
def deletar_produto_carrinho(nome):
    conexao, cursor = abrir_conn(banco)
    resultado = cursor.execute(deletar_prod, [nome]).rowcount
    if resultado:
        fechar_conn(conexao)
        return {"mensagem": f'{resultado} produto(s) removido(s)'}, 200
    else:
        return {"erro": "Produto não encontrado"}, 200

@app.route('/deleta_tudo', methods=['DELETE'])
def deletar_tudo_carrinho():
    conexao, cursor = abrir_conn(banco)
    resultado = cursor.execute(deletar_tudo).rowcount
    fechar_conn(conexao)
    return {"mensagem":"Todos os produtos foram removidos"}

#consultando produtos
@app.route('/consulta_tudo', methods=['GET'])
def consultar_tudo_carrinho():
    conexao, cursor = abrir_conn(banco)
    resultado = cursor.execute(consultar_tudo).fetchall()
    fechar_conn(conexao)
    return resultado, 200

#alterar quantidade
@app.route('/update/<quantidade>')
def update_quantidade(quantidade):
    consulta = consultar_nome_carrinho(quantidade)
    if consulta: 
        id=request.args.to_dict() 
        if id: 
            conexao, cursor = abrir_conn(banco)
            cursor.execute(update, quantidade)
            fechar_conn(conexao)
            return id
        else: 
            return render_template('alterar_quantidade.html', tabela_carrinho=consulta[0])
    else:
        return {'error': 'mensagem de erro'}

#consulta de itens
@app.route('/consulta/<nome>', methods=['GET'])
def consultar_nome_carrinho(nome):
    conexao, cursor = abrir_conn(banco)
    resultado = cursor.execute(consultar_nome, [nome]).fetchall()
    if resultado:
        fechar_conn(conexao)
        return resultado, 200
    else:
        return {"erro":"Produto não registrado"}

if __name__ == '__main__':
    app.run(debug=True)
