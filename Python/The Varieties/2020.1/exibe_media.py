def bem_vindo():
    print('Bem-vindo! Vamos calcular a média')

def exibe_media(num1, num2, num3):
    soma = num1 + num2 + num3
    print(soma / 3)

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

bem_vindo()

exibe_media(a, b, c)

