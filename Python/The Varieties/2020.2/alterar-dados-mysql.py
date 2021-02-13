import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

connection.execute("update FUNCIONARIO set NOME='Maria Juliana' where ID=2")

connection.close()
