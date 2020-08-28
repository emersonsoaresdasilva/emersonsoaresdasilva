A = int(input())
B = int(input())
Q = 0 # Quociente da divisão inteira de A por B.

while A >= B:
    A -= B
    Q += 1
print('O quociente é:', Q)
print('O resto da divisão é:', A)
