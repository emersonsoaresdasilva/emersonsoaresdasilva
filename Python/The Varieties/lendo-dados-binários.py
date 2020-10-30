#Para ler dados do arquivo binário, utilizamos a função load() do módulo pickle.
import pickle

class Pessoa:
    def __init__(self, nome, ano, altura):
        self.nome = nome
        self.ano = ano
        self.altura = altura

f = open('arquivo.dat', 'rb') #Modo 'rb': read bytes
pessoa = pickle.load(f)
f.close()
print(
    'Nome:',pessoa.nome,
    '\nAno nascimento:',pessoa.ano,
    '\nAltura:',pessoa.altura
)
