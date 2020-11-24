#Múltiplas Listas.
'''
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número do serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for equipamento in equipamentos:
    print("Equipamento:", equipamento)
'''

#Um amigo chama "Índice".
'''
O índice é o número que define onde está armazenado um elemento dentro de uma lista.
Quando um primeiro append() é executado na lista, ele abre a posição 0 (zero) para armazenar o dado,
quando ele for executado novamente, abrirá a posição 1 (um) para o próximo dado, e assim sucessivamente.
'''

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número do serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento...:", (indice+1))
    print("Nome..........:", equipamentos[indice])
    print("Valor.........:", valores[indice])
    print("Serial........:", seriais[indice])
    print("Departamento..:", departamentos[indice])
    
'''
A estrutura do nosso “for” mudou, agora não estamos trabalhando com base nos elementos diretamente,
mas, sim, de acordo com o índice. Para a variável “índice” que criamos no “for”, será atribuído o valor de 0
até a quantidade de elementos que existirem dentro da nossa lista “equipamentos” (função “len()”),
que obviamente será a mesma quantidade de elementos que existirão nas listas.
'''

#Ainda com listas, podemos pesquisar um determinado dado:

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Serial.:", seriais[indice])

'''
Situação 1: todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo período) de 10%.
'''
#Alterando o valor de todos os equipamentos “impressora”.

depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo:", valores[indice])
        valores[indice] = valores[indice] * 0.9 #Desvalorização de 10%.
        print("Novo valor:", valores[indice])

'''
Situação 2: um equipamento com um determinado número serial foi danificado e será descartado.
Dica: para eliminar um item de uma lista, você utilizará o comando “del”. Exemplo: del lista[<indice>]
'''
#Eliminando o equipamento da lista.
serial = int(input("\nDigite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
