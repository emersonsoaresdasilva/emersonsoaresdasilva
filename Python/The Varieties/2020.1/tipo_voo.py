'''Escreva o fluxograma de um programa que tenha como entrada o tipo
do vôo ('N' para noturno e 'D' para diurno) e a quantidade de pessoas;
calcule e mostre a tarifa e o total a pagar de acordo com as condições abaixo:
'''

#Exemplo supondo que o usuário insira somente os tipos determinadados: Diurno (D) e Noturno (N).
Voo = input("Tipo do vôo: ")
Quantidade = int(input("Quantidade: "))

#Se o usuário inserir "D" vôo diurno.
if(Voo=='D'):
    if(Quantidade<=50):
        Total = Quantidade * 200.0
    else:
        Total = Quantidade * 120.00
#Se o usuário não inserir "D" o vôo vai ser obrigatoriamente "N" noturno.
else:
    if(Quantidade<=50):
        Total = Quantidade * 100.0
    else:
        Total = Quantidade * 80.00
print("R$ %.2F"%Total)

#Versão do programa em função!

'''

def calcula_preco(Voo, Quantidade):
#Se o usuário inserir "D" vôo diurno.
    if(Voo=='D'):
        if(Quantidade<=50):
            Total = Quantidade * 200.0
        else:
            Total = Quantidade * 120.00
#Se o usuário não inserir "D" o vôo vai ser obrigatoriamente "N" noturno.
    else:
        if(Quantidade<=50):
            Total = Quantidade * 100.0
        else:
            Total = Quantidade * 80.00
    print("R$ %.2F"%Total)
    return
'''
