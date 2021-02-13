f = open('gravando-dados-binários-listas.py', 'r')
num = 1
for linha in f:
    print(f'Linha {num}:',linha.rstrip())
    num += 1
f.close()
    
    
