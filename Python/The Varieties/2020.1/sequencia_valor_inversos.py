# Lista de valores:
valores = []
i = 0
# Executa até ocorrer `break`
while i < 10:

    # Pede ao usuário um valor inteiro:
    novo = int(input())    

    # Se não, adiciona o valor a lista:
    valores.append(novo)
    i += 1

# Percorre toda a lista de trás para frente:
for i in reversed(valores):

    # Exibe o valor na tela:
    print(i)
