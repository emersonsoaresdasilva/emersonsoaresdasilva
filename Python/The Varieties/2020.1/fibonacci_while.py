a = 1
b = 1
n = int(input('n: '))
cont = 0
while cont < n:
    print(a, end=' ')
    b = b + a
    a = b - a
    cont += 1
