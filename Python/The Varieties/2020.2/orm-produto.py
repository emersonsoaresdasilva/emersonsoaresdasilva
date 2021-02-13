'''
Object-Relational Mapping (ORM) é uma técnica para aproximar o paradigma de
programação orientada a objetos ao paradigma do banco de dados relacional.

• Técnica muito empregada nos  últimos anos.
• Vantagens:
- Permite abstrair o código de SQL;
- Aproxima o paradigma de POO ao paradigma de banco de dados relacional;
- Aumenta a produtividade;
'''
import pymysql
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("mysql+pymysql://root:1903123@localhost:3306/lp2") #Criar conexão com o MySQL.
connection = engine.connect()
Base = declarative_base(engine) #Instancia da classe Base.
session = Session() #Criação da sessão.

connection.execute("""
CREATE TABLE IF NOT EXISTS PRODUTO (
    COD int NOT NULL,
    COD_FABRICANTE int NOT NULL,
    NOME varchar(100) NOT NULL,
    MODELO varchar(50) NOT NULL,
    PRECO float NOT NULL,
    TEMPO_GARANTIA int NOT NULL,
    PRIMARY KEY (COD)
)
""")
class Produto(Base):
    __tablename__ = 'PRODUTO'
    id = Column('COD', Integer, primary_key=True)
    cod_fabricante = Column('COD_FABRICANTE', Integer)
    nome_produto = Column('NOME', String(100))
    modelo_produto = Column('MODELO', String(50))
    preco = Column('PRECO', Integer)
    tempo_garantia = Column('TEMPO_GARANTIA', Integer)

    def __init__(self, id, cod_fabricante, nome_produto, modelo_produto, preco, tempo_garantia):
        self.id = id
        self.cod_fabricante = cod_fabricante
        self.nome_produto = nome_produto
        self.modelo_produto = modelo_produto
        self.preco = preco
        self.tempo_garantia = tempo_garantia
        
connection.close()
