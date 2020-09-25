class Retangulo:
    def __init__(self, a, b):
        self.lado_a = a #Atributo 01.
        self.lado_b = b #Atributo 02.

    def get_lado_a(self):
        return self.lado_a

    def get_lado_b(self):
        return self.lado_b

    def set_lado_a(self, a):
        if a > 0:
            self.lado_a = a
        else:
            self.lado_a = 0

    def set_lado_b(self, b):
        if b > 0:
            self.lado_b = b
        else:
            self.lado_b = 0

#Programa principal:
ret1 = Retangulo(2, 4)
ret2 = Retangulo(3, 8)
ret1.set_lado_a(10)
print('O retângulo 1 possui lados:', ret1.get_lado_a(), 'e', ret1.get_lado_b())
print('O retângulo 2 possui lados:', ret2.get_lado_a(), 'e', ret2.get_lado_b())
