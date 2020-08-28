A = int(input())
B = int(input())
C = int(input())

if abs((B - C)< A < B + C) and abs((A - C)< B < A +C) and abs((A - B)< C <A + B):
    if A == B and B == C:
        print("Equilatero")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Nao eh triangulo")