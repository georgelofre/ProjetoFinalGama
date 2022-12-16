from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient
import pandas as pd #Para a consulta

app = Flask(__name__)

conn = MongoClient('mongodb+srv://ficastro:jornaldb132@cluster0.dyf7dpm.mongodb.net/test')
db = conn['Organicos']

#Início
@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))

#Cadastramento de produtos
@app.route('/cadastrar/', methods=['GET'])
def cadastrar():
    produto = request.args.to_dict()
    print(produto)
    if not produto: #Se não houver argumentos
        return redirect(url_for('static', filename='cadastrar.html'))
    else:
        query = db.produtos.find_one({'nome': produto['nome']})
        if query: #Se o produto já está no banco
            return redirect(url_for('static', filename='ja_cadastrado.html'))
        else: #Se o produto não está no banco
            db.produtos.insert_one(produto)
            del produto['_id']
            return redirect(url_for('static', filename='cadastrado.html'))


#Consulta de produtos
@app.route('/consultar/')
def consultar():
    produto = request.args.to_dict()
    if not produto:
        produtos = list(db.produtos.find())
        print(produtos)
        return render_template('consultar.html', produtos=produtos)
    else:
        produto = db.produtos.find_one({'nome': produto['nome']}, {'_id':False})
        print(produto)
        if produto: #Se produto está no banco
            prodNome = produto['nome'].capitalize()
            prodPreco = float(produto['preco'])
            prodDesc = produto['descricao'].capitalize()
            return render_template('consultado.html',prodNome=prodNome,prodPreco=prodPreco,prodDesc=prodDesc)

    
#Deletar produtos
@app.route('/deletar/')
def deletar_nome():
    produto = request.args.to_dict()
    if not produto:
        produtos = list(db.produtos.find())
        print(produtos)
        return render_template('deletar.html', produtos=produtos)
    else:
        produto = db.produtos.find_one({'nome': produto['nome']}, {'_id':False})
        print(produto)
        if produto:
            db.produtos.delete_one({'nome': produto['nome']})
            return redirect(url_for('static', filename='deletado.html'))

#Atualizar preço e descrição
@app.route('/atualizar/')
def atualizar():
    produto = request.args.to_dict()
    if not produto:
        produtos = list(db.produtos.find())
        print(produtos)
        return render_template('atualizar.html', produtos=produtos)
    else:
        db.produtos.update_one(
            {'nome': produto['nome']},
            {'$set':
                {'preco': produto['preco'],
                'descricao': produto['descricao']}
            }
        )
        return redirect(url_for('static', filename='atualizado.html'))


if __name__ == '__main__':
    app.run(debug=True) 