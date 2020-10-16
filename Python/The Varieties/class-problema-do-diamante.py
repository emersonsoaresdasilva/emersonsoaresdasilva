class Ingles(object):
    def saudacao(self):
        print('Hi!')

class Portugues(object):
    def saudacao(self):
        print('Olá!')

class Bilingue(Ingles, Portugues):
    pass

# Programa principal:
b = Bilingue()
b.saudacao()
