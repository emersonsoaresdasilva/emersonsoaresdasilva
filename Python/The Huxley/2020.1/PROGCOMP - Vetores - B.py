valores = []
i = 0
while i < 10:
    novo = int(input())    
    valores.append(novo)
    i += 1
    
for i in reversed(valores):
    print(i)