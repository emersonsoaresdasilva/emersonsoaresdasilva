import pymysql
import sqlalchemy
engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")

connection = engine.connect()
connection.execute("delete from FUNCIONARIO where ID=2")

connection.close()
