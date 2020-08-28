#--------------------
# Versão com while!
#--------------------

idades = [9,8,6,10,7,3,2]
pos = 0
while pos < 7:
    print('valor da posição =', pos)
    pos += 1

#--------------------
# Versão com for!
#--------------------

#Nós mesmo contamos a quantidades de itens do vetor.
idades = [9,8,6,10,7,3,2]
for pos in range(7): # [0..7[
    print('valor da posição', pos, '=', idades[pos])

#Identifica o tamanho do vetor automaticamente.
idades = [9,8,6,10,7,3,2]
for pos in range(len(idades)): # [0..7[
    print('valor da posição', pos, '=', idades[pos])
