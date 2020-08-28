Quantidade = int(input('Quantidade: '))

if(Quantidade<=12):
    print('Total: R$ %.2F' % (Quantidade * 1.30))
else:
    print('Total: R$ %.2F' % Quantidade)
