import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2") #Configurando a conexão.
connection = engine.connect() #Conectando ao SGBD.

#Aqui colocamos instruções para manipular o BD: consultar, inserir, alterar, excluir, etc.

connection.close() #Encerrando a conexão com o SGBD.
