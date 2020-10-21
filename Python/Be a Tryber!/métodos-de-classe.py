#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 10 |
#       Métodos de Classe (Trybe)
#-------------------------------------
class Impressora:
    def __init__(self):
        self.a = 10
    
    @classmethod
    def imprimir_folha(cls): #Método de classe - cls.
        print('Folha impressa')

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

    @classmethod
    def imprimir_a(cls):
        print(cls.a)

Impressora.imprimir_folha()

print('='*15)
Impressora.imprimir_livro(5)

print('='*15)
impressora = Impressora()
impressora.imprimir_folha()

