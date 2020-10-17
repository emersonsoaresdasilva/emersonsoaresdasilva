#-------------------------------------
# CURSO BÁSICO DE PYTHON | AULA 07 |
#           Herança (Trybe)
#-------------------------------------

class Animal:
    def fazer_barulho(self):
        print('Barulho de um animal.')

class Domestico():
    def esta_dormindo(self):
        return True

class Mamifero(Animal):
    pass

class Cachorro(Mamifero, Domestico):
    def enterrar_osso(self):
        print('O osso foi enterrado.')

class Gato(Mamifero):
    def fazer_barulho(self):
        print('Miau... Miau!')

gato = Gato()
gato.fazer_barulho()

cachorro = Cachorro()
cachorro.fazer_barulho()
print(cachorro.esta_dormindo())
cachorro.enterrar_osso()
