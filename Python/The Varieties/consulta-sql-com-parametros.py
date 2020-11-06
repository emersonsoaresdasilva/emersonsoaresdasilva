import pymysql

import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

id_func = int(input('Informe o ID do usuario: '))
t = sqlalchemy.text("select * from FUNCIONARIO where ID=:id")
resultado = connection.execute(t, id=id_func)

for linha in resultado:
    print(linha)
connection.close()
