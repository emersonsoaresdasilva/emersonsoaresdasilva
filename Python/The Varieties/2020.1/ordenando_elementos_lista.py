lista = [4, 1, 3, 5, 2]

n = len(lista) #Pegar comprimento da lista

#Percorrer todos os elementos da lista
for i in range(n):

    #Para cada elemento "i" da lista
    #percorra todos os elementos que está a direita
    for j in range(n - i - 1):

        #se o elemento a esquerda for maior
        #que o elemento da direita
        if lista[j] > lista[j + 1]:

            #realiza a troca com o
            #auxilio da variavel "aux"
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
print(lista) #Saída: [1, 2, 3, 4, 5]
