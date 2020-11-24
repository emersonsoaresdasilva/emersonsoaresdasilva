'''
A estrutura “while” é a mais comum entre os programadores,
e normalmente a primeira que se aprende. Ela funciona basicamente como um “if”,
mas com a diferença que executará o seu bloco de códigos enquanto a condição for verdadeira
e não somente uma vez, ou seja, a condição será testada enquanto não for falsa.
Podemos dizer que o fluxo do código seguirá a seguinte sequência:
'''

#While "infinito".
numero = int(input("Digite um numero: "))
while numero < 100:
    print("\t" + str(numero))
    numero = numero + 1
print("Laço encerrado....")


#Desafio de Decisão.
resposta = "SIM"
while resposta == "SIM":
    nivel = input("Digite o nível de acesso: ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite o seu gênero: ").upper()
        if nivel == "ADM":
            if genero == "FEMININO":
                print("Olá administradora")
            else:
                print("Olá administrador")
        else:
            if genero == "FEMININO":
                print("Olá usuária")
            else:
                print("Olá usuario")
    elif nivel == "GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta = input("Digite SIM para continuar: ").upper()


#Desafio de Encadeamento.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")

'''
A estrutura “for” também permite uma repetição, mas sua aplicação é um tanto quanto diferente quando
comparada ao “while”. O “for” indica o término do laço de duas formas básicas: por um número que
delimita o seu final ou por uma lista de dados que foi verificada por completo.
'''
#For "infinito".
for numero in range(1,int(input("Digite um numero para determinar o fim: ")),1):
    print ("\t" + str(numero))

#Script de tabuada.
tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número:", tabuada)
for valor in range(1,11,1): #1...10 de 1.
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
