cartas = []
dias = 0
meta = 0

while dias < 7:
    quantidade = int(input())
    cartas.append(quantidade)
    if quantidade >= 100:
        meta += 1        
    dias += 1
print(meta)
print(f'{sum(cartas)/dias:.0f}')

