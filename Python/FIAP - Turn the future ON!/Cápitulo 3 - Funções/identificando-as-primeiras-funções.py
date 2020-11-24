#Identificando as primeiras funções.
'''
inventario=[]
resposta = "S"

#adicionar item no inventario
while resposta == "S":
    equipamento=[input("Equipamento: "),
                  float(input("Valor: ")),
                  int(input("Número Serial: ")),
                  input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

#exibir dados do inventário
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#localizar um item no inventario
busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

#depreciar itens no inventario
depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

#excluir um item do inventario
serial=int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

#exibir dados do inventário
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#resumo de valores do inventário
valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))
'''

#Para criarmos funções, utilizaremos o comando “def”, e a estrutura básica de uma função é a seguinte:
'''
def <identificador da funcao> (<parametro(s)>):          
    <código que será executado>
    return <Dado que será retornado, caso seja necessário>
'''

#Para a nossa função preencherInventario(), recebemos um parâmetro que é a lista na qual o módulo principal irá armazenar os itens do inventário.
def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento=[input("Equipamento: "),
                      float(input("Valor: ")),
                      int(input("Número Serial: ")),
                      input("Departamento: ")]
        inventario.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()

#A nossa função “exibirInventario()”irá receber a lista, por parâmetro, e, então, executará o laço “for” para exibir os dados da lista recebida.
def exibirInventario(lista):
    for elemento in inventario:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

#A função depreciarPorNome() apresenta dois parâmetros: um deles é a lista na qual estão os equipamentos que sofrerão a depreciação; e o outro é a porcentagem que se deseja depreciar.
def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])

#A função excluirPorSerial() retorna uma string, ou seja, quando formos chamar essa função, devemos fazê-la dentro de um comando print(), para que possamos ver a mensagem.
def excluirPorSerial(lista):
    serial=int(input("\nDigite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
    return "Itens excluídos."

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
