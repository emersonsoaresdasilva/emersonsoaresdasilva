A = int(input())
B = int(input())
C = int(input())

if abs((B - C)< A < B + C) and abs((A - C)< B < A +C) and abs((A - B)< C <A + B):
    if A == B and B == C:
        print("podem formar um triangulo")
        print("equilatero")
    elif A == B or B == C or A == C:
        print("podem formar um triangulo")
        print("isosceles")
    else:
        print("podem formar um triangulo")
        print("escaleno")
else:
    print("nao podem formar um triangulo")