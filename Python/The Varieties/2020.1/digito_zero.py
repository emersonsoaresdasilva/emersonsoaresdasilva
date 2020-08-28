a = int(input())
b = int(input())
cont = a
if a >= b:
    while cont > b + 1:
        cont -= 1
        a -= 1
        print(cont)
'''
Entrada:
4
0

Saída:
3
2
1
'''
