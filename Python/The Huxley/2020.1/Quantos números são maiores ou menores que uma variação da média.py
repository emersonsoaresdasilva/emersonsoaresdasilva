n = int(input())
notas = []
acima = 0
baixo = 0

for x in range(n):
    notas.append(float(input()))
media = sum(notas) / len(notas)

for n in notas:
    if n > media * 1.10:
        acima += 1
    elif n < media * 0.90:
        baixo += 1
print('%.2F'%media)
print(acima)
print(baixo)