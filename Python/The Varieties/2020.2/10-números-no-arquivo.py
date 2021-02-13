f = open('10-números-no-arquivo.txt', 'a')
v = ','
p = '.'

print('Informe 10 números: ')
for i in range(10):
    numero = input('Insira um número: ')
    if i == 9:
        f.write(f'%s{p}' % (numero))
    else:
        f.write(f'%s{v}' % (numero))
print('Os 10 números foram inseridos.')
f.close()
