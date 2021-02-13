class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        return '...'
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self): # Método da superclasse reescrito na classe filha
        return 'Miau!'

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self): # Método da superclasse reescrito na classe filha
        return 'Au au!'

#Programa principal:
gato = Gato('Garfield')
cachorro = Cachorro('Milou')
rinoceronte = Animal('Cacareco')

animais  = [gato, cachorro, rinoceronte]

for animal in animais:
    print(animal.nome + ':', animal.falar())

