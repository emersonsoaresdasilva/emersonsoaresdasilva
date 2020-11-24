#Decisões Simples.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

prioridade = "NÃO"
if idade >= 65:
    prioridade = "SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

#Decisões Compostas.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
    
#um “=” representa atribuição, dois “==” representa comparação.
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")

#Vamos utilizar os operadores “AND” ou “OR”.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

#Decisões encadeadas.
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

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
