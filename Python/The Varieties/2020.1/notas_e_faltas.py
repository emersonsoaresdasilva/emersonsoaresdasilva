Nota = float(input("Digite sua nota: "))
Faltas = int(input("Digite suas faltas: "))

if(Nota>7 and Faltas<5):
    print("Você está aprovado!\n")
else:
    print("Você está reprovado!\n")

while True:
    Nota = float(input("Digite sua nota: "))
    Faltas = int(input("Digite suas faltas: "))

    if(Nota>7 and Faltas<5):
        print("Você está aprovado!\n")      
    else:
        print("Você está reprovado!\n")

#Definindo função para o código acima:
#def nota_falta():
#Código desenvolvido anteriormente, sem o while True[...]
#return
