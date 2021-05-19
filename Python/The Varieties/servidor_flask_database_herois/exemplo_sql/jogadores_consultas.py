from sqlalchemy import create_engine
from sqlalchemy.sql import text

#eu nao estou usando um servidor, como MySQL,
#ou postgres.
#estou usando essa biblioteca sqlite3, 
#que cria meu banco de dados em um arquivo.
#tanto que eu posso mandar esse arquivo para o site
#sqliteonline.com e todos os dados estão lá

engine = create_engine('sqlite:///rpg.db')


class JogadorNaoExisteException(Exception):
    pass

def consultar_jogador(id_j):
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador WHERE id = :id_j""") #query com "buraco" com o nome id_j
        rs = con.execute(statement, id_j=id_j) #e usei esse buraco
        jogador = rs.fetchone() #pega a primeira linha
        if jogador == None: #se nao tinha nenhuma linha, jogador vale none
            raise JogadorNaoExisteException
        return dict(jogador) #converte o jogador para dicionário
        

def conta_jogadores():
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador""") #todos os jogadores
        rs = con.execute(statement) 
        jogadores = 0
        while (rs.fetchone() != None): #Pego um jogador. Uma linha da tabela. Se acabaram os jogadores, vou receber um None
            jogadores += 1
        return jogadores

#segunda versao, tb funciona
def conta_jogadores():
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador""") #todos os jogadores
        rs = con.execute(statement) 
        jogadores = len(rs.fetchall()) #fetchall é perigoso. Monta uma lista com todos os resultados. Pode encher a sua RAM
        return jogadores

def jogador_por_email(email):
    with engine.connect() as con:    
        statement = text ("""SELECT * FROM Jogador WHERE email = :email""")
        rs = con.execute(statement, email=email) 
        jogador = rs.fetchone() 
        if jogador == None: 
            raise JogadorNaoExisteException
        return dict(jogador) 



