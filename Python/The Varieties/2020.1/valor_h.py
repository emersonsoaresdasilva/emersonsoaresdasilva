'''
Escreva um programa que calcule o valor de H, sendo que ele é determinado
pela série H = 1/1 + 3/2 + 7/4 + 11/6 + 15/8 + 19/10 + ... + 99/50.
'''
#Numerador C1 e Denominador C2: 1N/D1, 3N/D2 [...]
H = 1
Denominador = 2

for Numerador in range(3, 100, 4):
    H += Numerador / Denominador
    Denominador += 2
print(H)
    
