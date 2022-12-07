from flask import Flask

app = Flask(__name__)

@app.route('index_relatorio')
def index_rel():
    return 'oi'