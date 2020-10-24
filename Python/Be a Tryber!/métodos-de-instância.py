#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 11 |
#   Métodos de Instância (Trybe)
#-------------------------------------

class Impressora:
    modelo = 'HP'
    def __init__(self, numero_folhas):
        self.numero_folhas = numero_folhas

    def imprimir_folha(self):
        print('Folha impressa')

    def imprimir_livro(self, paginas):
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas -= 1
        else:
            print('Número de folhas insuficiente!')
            print(f'Por gentileza, verifique a bandeja de folhas de sua impressora {Impressora.modelo}.')

    def quantidade_folhas(self):
        print(f'Quantidade de folhas restantes: {self.numero_folhas}.')
        if self.numero_folhas == 0:
            print(f'Por gentileza, verifique a bandeja de folhas de sua impressora {Impressora.modelo}.')
            
    @classmethod
    def print_modelo(cls):
        print(cls.modelo)

    def print_modelo_instancia(self):
        print(self.modelo)

impressora = Impressora(10)
impressora.imprimir_livro(10)
impressora.quantidade_folhas()

'''
impressora.print_modelo()
impressora.print_modelo_instancia()
'''
