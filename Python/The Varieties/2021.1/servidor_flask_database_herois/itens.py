import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def item_existe(id):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM Item WHERE id = {id}'
        resultado = conexao.execute(sql, id=id)
        item = resultado.fetchone() # Pegando a primeira linha.
        return False if item is None else True

def consultar_item(id):
    if item_existe(id):
        with engine.connect() as conexao:
            sql = f'SELECT * FROM Item WHERE id = {id}'
            resultado = conexao.execute(sql, id=id)
            item = resultado.fetchone() # Pegando a primeira linha.
            return False if id is None else dict(item)
    else:
        raise ItemNaoExisteException

def nome_para_id_item(item):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM Item WHERE nome = "{item}"'
        resultado = conexao.execute(sql, id=id)
        item = resultado.fetchone() # Pegando a primeira linha.
        return False if item is None else item[0] # ID do item.

def criar_item(tipo, nome, fisico, agilidade, magia):
    with engine.connect() as conexao:    
        sql = f'INSERT INTO Item (tipo, nome, fisico, agilidade, magia) VALUES ("{tipo}", "{nome}", {fisico}, {agilidade}, {magia})'
        conexao.execute(sql, tipo=tipo, nome=nome, fisico=fisico, agilidade=agilidade, magia=magia)

def colocar_item_em_uso_banco(heroi, item):
    with engine.connect() as conexao:
        sql = f'UPDATE Item SET emUso = 1 WHERE id = {item}'
        conexao.execute(sql, item=item, heroi=heroi)