import pickle

class Pessoa:
    def __init__(self, nome, ano, altura):
        self.nome = nome
        self.ano = ano
        self.altura = altura

f = open('arquivo.dat', 'rb') #Modo 'rb': read bytes.

lista = pickle.load(f)
f.close()

for pessoa in lista:
    print(pessoa.nome, pessoa.ano, pessoa.altura)
