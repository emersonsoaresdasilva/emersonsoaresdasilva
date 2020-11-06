import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

id_func = int(input('ID do funcion ́ario: '))
nome_func = input('Nome do funcion ́ario: ')
idade_func = int(input('Idade do funcion ́ario: '))
salario_func = float(input('Sal ́ario do funcion ́ario: '))
t = sqlalchemy.text("insert into FUNCIONARIO values (:id, :nome, :idade, :salario)")
connection.execute(t, id=id_func, nome=nome_func, idade=idade_func, salario=salario_func)

connection.close()
