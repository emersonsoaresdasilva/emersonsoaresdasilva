from sqlalchemy import create_engine
from sqlalchemy.sql import text

class NotFoundError(Exception):
    pass

class IncompatibleError(Exception):
    pass

engine = create_engine('sqlite:///tinder.db')

with engine.connect() as conexao:    
    create_pessoas = '''
    CREATE TABLE IF NOT EXISTS Pessoa (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        sexo TEXT,
        busca_homem BOOL,
        busca_mulher BOOL
    )
    '''
    create_interesses = '''
    CREATE TABLE IF NOT EXISTS Interesse (
        id_interessado INTEGER,
        id_alvo INTEGER,
        FOREIGN KEY (id_interessado) REFERENCES Pessoas(id),
        FOREIGN KEY (id_alvo) REFERENCES Pessoas(id)
    )
    '''
    resposta = conexao.execute(create_pessoas)
    resposta = conexao.execute(create_interesses)

def adiciona_pessoa(dic_pessoa): 
    with engine.connect() as conexao:
        sql = f'INSERT INTO Pessoa (nome, id) VALUES (:nome, :id)'
        conexao.execute(sql, nome=dic_pessoa['nome'], id=dic_pessoa['id'])

def todas_as_pessoas():
    with engine.connect() as conexao:    
        sql = 'SELECT * FROM Pessoa'
        resposta = conexao.execute(sql)
        pessoas = []
        while True:
            linha = resposta.fetchone()
            if linha == None:
                break
            pessoas.append(dict(linha))
        return pessoas

def localiza_pessoa(id_pessoa):
    with engine.connect() as conexao:    
        sql = 'SELECT * FROM Pessoa WHERE id = :id'
        resposta = conexao.execute(sql, id=id_pessoa)
        pessoa = resposta.fetchone()
        if pessoa is None:
            raise NotFoundError
        return dict(pessoa)

def consulta_interesses(id_interessado):
    with engine.connect() as conexao:
        sql = f'SELECT id_alvo FROM Interesse WHERE id_interessado = {id_interessado}'
        resposta = conexao.execute(sql, id_interessado=id_interessado)
        interesses = []
        while True:
            alvo_interesse = resposta.fetchone()
            if alvo_interesse is None:
                break
            interesses.append(alvo_interesse[0])
        return interesses    

def reseta():
    with engine.connect() as conexao:   
        sql = 'DELETE FROM Pessoa' 
        conexao.execute(sql)
        sql = 'DELETE FROM Interesse'
        conexao.execute(sql)

def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    with engine.connect() as conexao:
        sql = 'INSERT INTO Interesse (id_interessado, id_alvo) VALUES (:id_i, :id_a)'
        conexao.execute(sql, id_i=id_interessado, id_a=id_alvo_de_interesse)

def remove_interesse(id_interessado, id_alvo_de_interesse):
    with engine.connect() as conexao:
        sql = 'DELETE FROM Interesse WHERE id_interessado = :id_interessado and id_alvo = :id_alvo'
        conexao.execute(sql, id_interessado = id_interessado, id_alvo = id_alvo_de_interesse)
      
def lista_matches(id_pessoa):
    if localiza_pessoa(id_pessoa):
        lista_dos_matches = []
        for id_pessoa2 in consulta_interesses(id_pessoa): 
            if id_pessoa in consulta_interesses(id_pessoa2):
                lista_dos_matches.append(id_pessoa2)
        return lista_dos_matches
