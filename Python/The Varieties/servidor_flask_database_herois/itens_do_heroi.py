import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def heroi_tem_item(id):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM ItemDoHeroi WHERE idHeroi = {id}'
        resultado = conexao.execute(sql, id=id)
        heroi = resultado.fetchone() # Pegando a primeira linha.
        return False if heroi is None else True

def heroi_quantos_itens(id):
    with engine.connect() as conexao:
        sql = f'SELECT * FROM ItemDoHeroi WHERE idHeroi = {id}'
        resultado = conexao.execute(sql, id=id)
        return len(resultado.fetchall())

def itens_do_heroi(id):
    with engine.connect() as conexao:
        sql = f'''
            SELECT tipo, magia from Item 
            JOIN ItemDoHeroi
            ON ItemDoHeroi.iditem = Item.id
            WHERE ItemDoHeroi.idheroi = {id}
        '''
        resultado = conexao.execute(sql, id=id)
        registros = resultado.fetchall()
        itens_heroi = []
        for linha in registros:
            itens_heroi.append({'tipo': linha['tipo'], 'magia': linha['magia']})
        return itens_heroi

def itens_em_uso_do_heroi(id):
    with engine.connect() as conexao:
        sql = f'''
            SELECT tipo, magia from Item
            JOIN ItemDoHeroi
            ON ItemDoHeroi.iditem = Item.id
            WHERE ItemDoHeroi.idheroi = {id} AND Item.emUso = 1
        '''
        resultado = conexao.execute(sql, id=id)
        return resultado.fetchall()

def itens_em_uso_por_nome_do_heroi(nome):
    with engine.connect() as conexao:
        sql = f'''
            SELECT Item.tipo, Item.magia, Item.fisico, Item.agilidade FROM Item
            JOIN ItemDoHeroi
            ON ItemDoHeroi.idItem = Item.id
            INNER JOIN Heroi
            ON ItemDoHeroi.idHeroi = Heroi.id
            WHERE Heroi.nome = "{nome}" AND Item.emUso = 1
        '''
        resultado = conexao.execute(sql, nome=nome)
        return resultado.fetchall()
        
def dar_item_para_heroi_banco(heroi, item):
    with engine.connect() as conexao:
        sql = f'INSERT INTO ItemDoHeroi (iditem, idheroi) VALUES ({item}, {heroi})'
        conexao.execute(sql, item=item, heroi=heroi)