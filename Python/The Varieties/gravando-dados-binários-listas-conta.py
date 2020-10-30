import pickle

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

conta1 = Conta(12345, 'Emerson Soares da Silva', 5000.00)
conta2 = Conta(67890, 'Maria dos Santos', 999.99)
conta3 = Conta(15846, 'Eduarda Batista Lima', 100.000)

lista = [conta1, conta2, conta3]

f = open('arquivo_pickle.dat', 'wb')
pickle.dump(lista, f)
f.close()
    

    
