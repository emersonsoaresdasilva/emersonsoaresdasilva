import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2")
connection = engine.connect()

connection.execute("""
CREATE TABLE IF NOT EXISTS FUNCIONARIO(
    ID int NOT NULL,
    NOME varchar(255) NOT NULL,
    IDADE int NOT NULL,
    SALARIO float NOT NULL,
    PRIMARY KEY (ID)
)
""")
connection.close()
