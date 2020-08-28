Soma = 0
Quantidade = 0
Nota = float(input())

while Nota != -1:
    Soma += Nota
    Quantidade += 1
    Nota = float(input())
print("%.2f"%(Soma/Quantidade))