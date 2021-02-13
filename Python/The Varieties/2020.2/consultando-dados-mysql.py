import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

resultado = connection.execute("select * from FUNCIONARIO order by ID")
for linha in resultado:
    #print(linha)
    id, nome, idade, salario = linha
    print(id, nome, idade, salario)
    
connection.close()
