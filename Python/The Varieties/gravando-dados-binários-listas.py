#E possível gravar objetos, listas, dicionários e outras estruturas de dados mais complexas em arquivo utilizando o módulo pickle.
import pickle

class Pessoa:

    def __init__(self, nome, ano, altura):
        self.nome = nome
        self.ano = ano
        self.altura = altura

pessoa1 = Pessoa('Emerson', 2001, 1.70)
pessoa2 = Pessoa('Igor', 2500, 1.75)
pessoa3 = Pessoa('Guilherme', 1750, 2.00)
lista = [pessoa1, pessoa2, pessoa3]

f = open('arquivo.dat', 'wb')

pickle.dump(lista, f)
f.close()
