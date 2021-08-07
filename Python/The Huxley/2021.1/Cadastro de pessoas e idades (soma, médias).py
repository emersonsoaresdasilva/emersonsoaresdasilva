import math
import statistics

nomes = []
idades = []

for i in range(5):
    nomes.append(input())
    idades.append(int(input()))
    print(f'Pessoa: {nomes[i]} , {idades[i]}')

media_geometrica = round(statistics.geometric_mean(idades), 1)             
print(sum(idades))
print(sum(idades) / len(idades))
print(math.trunc(media_geometrica))
                  
