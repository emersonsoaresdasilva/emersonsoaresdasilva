class Retangulo:
    def __init__(self, a, b):
        self.lado_a = a #Atributo 01.
        self.lado_b = b #Atributo 02.

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return (2 * self.lado_a) + (2* self.lado_b)


#Programa principal:
comprimento = float(input('Informe o comprimento do retângulo: '))
largura = float(input('Informe a largura do retângulo: '))

calculo = Retangulo(comprimento, largura)

print('A área do retangulo é:', calculo.calcular_area())
print('O perímetro do retângulo é:', calculo.calcular_perimetro())
