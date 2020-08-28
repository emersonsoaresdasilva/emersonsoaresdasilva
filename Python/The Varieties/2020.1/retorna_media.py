def bem_vindo():
    print('Bem-vindo! Vamos calcular a média')

def retorna_media(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma / 3

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

bem_vindo()

resposta = retorna_media(a, b, c)

print('A média é %.2f' % resposta)
