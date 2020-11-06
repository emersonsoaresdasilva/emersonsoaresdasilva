import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

connection.execute("insert into FUNCIONARIO values (1, 'Pedro Jose', 27, 3000.00)")
connection.execute("insert into FUNCIONARIO values (2, 'Maria Joana', 31, 4500.00)")
connection.execute("insert into FUNCIONARIO values (3, 'Carolina Dias', 22, 2800.00)")

connection.close()
