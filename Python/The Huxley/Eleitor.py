idade = int(input())

if idade < 16:
    print('nao eleitor')
elif idade > 16 and idade < 18 or idade > 65:
    print('eleitor facultativo')
else:
    print('eleitor obrigatorio')

