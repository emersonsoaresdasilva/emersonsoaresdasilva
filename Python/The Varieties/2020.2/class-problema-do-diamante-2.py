class Tecnico(object):
    def __init__(self):
        self.id = 123
        self.nome = 'João'

class Cientista(object):
    def __init__(self):
        self.id = 456
        self.nome = 'Maria'

class Pessoa(Tecnico, Cientista):
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome

# Programa principal:
p = Pessoa()
print(p.get_id())
print(p.get_nome())
