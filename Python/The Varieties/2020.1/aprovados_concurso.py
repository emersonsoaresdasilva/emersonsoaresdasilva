C = 0
while True:
        P = int(input())
        if(P <= 0):
            print(C)
            break;
        M = int(input())
        R = float(input())
        if(P >= 40 < 50 and M >= 21 < 35 and R >=7.0):
                C += 1      
#Últuma tentativa abaixo - 19/04/2020 - Código negado!
'''
P = int(input("Português: "))
M = int(input("Matemática: "))
R = float(input("Redação: "))
C = 0
while (P >= 40 < 50 and M >= 21 < 35 and R >=7.0):
        C += 1
        P = int(input("Português: "))
        if(P < 0):
            print('Candidatos aprovados:',C)
            break;
        else:
          M = int(input("Matemática: "))
          R = float(input("Redação: "))
        if not (P < 40 and M < 21 < 35 and R <7.0):
            P = int(input("Português: "))
        if(P < 0):
            print('Candidatos aprovados:',C)
            break;
        else:
          M = int(input("Matemática: "))
          R = float(input("Redação: "))   
'''
'''
P = float(input("Português: "))
C = 0
if(P<0):
    print('Candidatos aprovados:',C)
else:
    M = int(input("Matemática: "))
    R = float(input("Redação: "))
    if(P >= 40 and M >= 21 and R >=7.0):
        C += 1
        print('Candidatos aprovados:',C)
    else:
        print('Candidatos aprovados:',C)
'''
'''
P = int(input("Português: "))
M = int(input("Matemática: "))
R = float(input("Redação: "))
C = 0
while (P >= 40 < 50 and M >= 21 < 35 and R >=7.0):
        C += 1
        P = int(input("Português: "))
        M = int(input("Matemática: "))
        R = float(input("Redação: "))
print('Candidatos aprovados:',C)
'''
