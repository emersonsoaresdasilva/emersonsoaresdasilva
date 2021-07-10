import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class HeroiNaoExisteException(Exception):
    pass

def heroi_existe(id):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM Heroi WHERE id = {id}'
        resultado = conexao.execute(sql, id=id)
        heroi = resultado.fetchone() # Pegando a primeira linha.
        return False if heroi is None else True

def consultar_heroi(id):
    if heroi_existe(id):
        with engine.connect() as conexao:
            sql = f'SELECT * FROM Heroi WHERE id = {id}'
            resultado = conexao.execute(sql, id=id)
            heroi = resultado.fetchone()
            return False if heroi is None else dict(heroi)
    else:
        raise HeroiNaoExisteException

def consultar_heroi_por_nome(nome):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM Heroi WHERE nome = "{nome}"'
        resultado = conexao.execute(sql, nome=nome)
        heroi = resultado.fetchone() # Pegando a primeira linha.
        return False if heroi is None else dict(heroi)

def criar_heroi_banco(nome, agilidade, fisico, magia):
    with engine.connect() as conexao:    
        sql = f'INSERT INTO Heroi (nome, agilidade, fisico, magia) VALUES ("{nome}", "{agilidade}", "{fisico}", "{magia}")'
        conexao.execute(sql, nome=nome, agilidade=agilidade, fisico=fisico, magia=magia)
