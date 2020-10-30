#Podemos gravar objetos diretamente em arquivos através do módulo pickle.

'''
Neste caso, estamos gravando dados binários (da mesma forma em que são armazenados na memória RAM do computador).
Portanto, não é possível ver o conteúdo do arquivo utilizando um editor de texto simples.
'''

#Para gravar os dados no arquivo, utilizamos a função dump() do módulo pickle como no exemplo a seguir:
import pickle

class Pessoa:

    def __init__(self, nome, ano, altura):
        self.nome = nome
        self.ano = ano
        self.altura = altura

pessoa = Pessoa('Emerson', 2001, 1.70)
f = open('arquivo.dat', 'wb')   #Modo 'wb': write bytes.
pickle.dump(pessoa, f)
f.close()
