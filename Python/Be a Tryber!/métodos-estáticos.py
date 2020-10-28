#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 12 |
#       Métodos Estáticos (Trybe)
#-------------------------------------
class Impressora:
    @staticmethod
    def ligar_para_suporte():
        print('Liguei para o suporte.')

    @classmethod
    def deu_problema_na_impressora(cls):
        print('Analisando o problema.')
        cls.ligar_para_suporte()

    def imprimir(self):
        print('Imprimindo página 01')
        self.ligar_para_suporte()

Impressora.ligar_para_suporte()

Impressora.deu_problema_na_impressora()

impressora = Impressora()

impressora.imprimir()
