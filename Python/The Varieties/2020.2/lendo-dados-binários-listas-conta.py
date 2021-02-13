import pickle

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

f = open('arquivo_pickle.dat', 'rb')

lista = pickle.load(f)
f.close()

for conta in lista:
    print('-'*15)
    print(f'Conta: {conta.numero}',
          f'\nTitular: {conta.titular}',
          f'\nSaldo: %.2f' %conta.saldo,
          )
