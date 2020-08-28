lista = []
while True:
    n = int(input())
    if n == 0:
        break;
    lista.append(n)
    media = int(sum(lista) / len(lista))
if media < 110:
    print('Glicose Normal')
elif media >= 200:
    print('Glicose Muito Alta')
else:
    print('Glicose Alterada')

