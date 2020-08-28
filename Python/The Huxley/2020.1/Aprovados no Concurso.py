Aprovados = 0
Portugues = int(input())

while Portugues >= 0:
    Matematica = int(input())
    Redacao = float(input())
    if(Portugues/50) >= 0.80 and (Matematica/35) >= 0.60 and Redacao >= 7:
        Aprovados += 1
    Portugues = int(input())
print(Aprovados)