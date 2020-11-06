'''
Object-Relational Mapping (ORM) é uma técnica para aproximar o paradigma de
programação orientada a objetos ao paradigma do banco de dados relacional.

• Técnicas muito empregadas nos  últimos anos.
• Vantagens:
- Permite abstrair o código de SQL;
- Aproxima o paradigma de POO ao paradigma de banco de dados relacional;
- Aumenta a produtividade;
'''
import pymysql
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/lp2") #Criar conexão com o MySQL.
connection = engine.connect()
Base = declarative_base(engine) #Instancia da classe Base.
session = Session() #Criação da sessão.

connection.execute("""
CREATE TABLE IF NOT EXISTS FUNCIONARIO (
    ID int NOT NULL,
    NOME varchar(255) NOT NULL,
    IDADE int NOT NULL,
    SALARIO float NOT NULL,
    PRIMARY KEY (ID)
)
""")
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, id, nome, idade, salario):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
#Inserir dados (um objeto)
func = Funcionario(1, 'Zezinho', 20, 1700) #Criar o objeto.
session.add(func)
session.commit() #Necessário fazer o commit()

#Inserir dados (lista de objetos)
func1 = Funcionario(2, 'Luizinho', 22, 1250)
func2 = Funcionario(3, 'Huguinho', 22, 2000)
lista = [func1, func2]
session.add_all(lista)
session.commit() #Necessário fazer o commit()

'''
Métodos principais para consultas de dados:
- .query(nome da classe): executa uma query na tabela mapeada pela classe
   informada no parâmetro;
- .all(): retorna todos os resultados da consulta realizada;
- .first(): retorna o primeiro resultado da consulta realizada;
- .get(valor): realiza a busca por um registro específico, de acordo com o
   valor informado (chave primária);
- .filter(): define o filtro a ser aplicado na consulta;
- .order by(): ordena a consulta realizada de acordo com o valor informado;
'''
print('-'*30)
print('Busca todos os dados da tabela')
result = session.query(Funcionario).all() #Retorna lista de objetos.
for i in result:
    print(i.id, i.nome, i.idade, i.salario)

print('-'*30)
print('Busca um dado específico (pela chave primária)')
func = session.query(Funcionario).get(2) #Busca pela chave primária e retorna o objeto.
print(func.id, func.nome, func.idade, func.salario)

print('-'*30)
print('Salario maior que 1500 (.all() para retornar todos)')
d = session.query(Funcionario).filter(Funcionario.salario>1500).order_by(Funcionario.nome).all()
for i in d:
    print(i.id, i.nome, i.idade, i.salario)

print('-'*30)
print('Busca utilizando v ́arios filtros (.all() para retornar todos)')
d = session.query(Funcionario).filter(Funcionario.idade == 22, Funcionario.nome.like('%inho%')).all()
for i in d:
    print(i.id, i.nome, i.idade, i.salario)

print('-'*30)
print('Busca utilizando filtros (.first() retorna apenas o primeiro)')
d = session.query(Funcionario).filter(Funcionario.idade == 22, Funcionario.nome.like('%inho%')).first()
print(d.id, d.nome, d.idade, d.salario)
'''
func = session.query(Funcionario).get(1) #Busca um objeto.
func.nome = 'Zezinho da Silva' #Altera os atributos do objeto.
func.idade = 25
session.commit() #Necessário o commit()
'''
'''
func = session.query(Funcionario).get(2) #Busca um objeto.
session.delete(func) #Deleta o objeto.
session.commit() #Necessário o commit()
'''
connection.close()
