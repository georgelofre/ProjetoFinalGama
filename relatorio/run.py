from app_mysql import create_app
from ProjetoFinalGama.relatorio.dadosbd.dadosdb import configteste, configreal

configdados = configreal

if __name__ == '__main__':
    create_app(configdados).run(debug=True)
