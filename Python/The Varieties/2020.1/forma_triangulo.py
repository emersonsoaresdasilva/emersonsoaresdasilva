A = int(input())
B = int(input())
C = int(input())


if abs((B - C)< A < B + C) and abs((A - C)< B < A +C) and abs((A - B)< C <A + B):
    print('sim')
else:
    print('nao')
