import mysql.connector as sql
from ProjetoFinalGama.relatorio.dadosbd.dadosdb import configreal, configteste

#configdados = configteste #cria banco de teste
configdados = configreal  #cria banco real

mydb = sql.connect(**configreal)
mycursor = mydb.cursor()

tabela = "CREATE TABLE if not exists `relatorio01` (`id` INT NOT NULL, `produto` VARCHAR(20) NULL, `quantidade` INT NULL, `valor` DECIMAL(4,2) NULL, PRIMARY KEY (`id`));"

linhas = ["INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('1', 'Banana', '4', '9.80');",
          " INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('2', 'Uva', '10', '15.20');",
          " INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('3', 'Jambo', '7', '14.75');",
          " INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('4', 'Tomate', '17', '23.60');"]

linhasteste = ["INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('1', 'Laranja', '4', '9.00');",
               "INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('2', 'Pessego', '11', '15.00');",
               "INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('3', 'Jambo', '7', '14.00');",
               "INSERT INTO `relatorio01` (`id`, `produto`, `quantidade`, `valor`) VALUES ('4', 'Limao', '19', '23.00');"]



mycursor.execute(tabela)

for c in range(0, len(linhas)):
    mycursor.execute(linhas[c])
    print(linhas[c])


print('Tabelas e linhas adicionadas!!!')

mydb.commit()

mycursor.close()

mydb.close()
