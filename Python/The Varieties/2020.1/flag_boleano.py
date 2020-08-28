'''
Crie um programa que receba como entrada um número natural e
exiba a quantiade de dígitos do valor dado.
Verifique se o valor dado obdece a condição de entrada e
repita a leitura até o que usuário informe um número correto.
'''


#Modelo Inicial do Programa
'''
N = int(input('N: '))

while (N < 0):
    N = int(input('Digite N novamente: '))
print(N)
'''

#Modelo Secundário do Programa - Validação da Entrada!
Valido = False
while not Valido: #Só vai resultar True quando valido == false.
    N = int(input('N: '))
    if (N >= 0):
        Valido = True
print(N)

#Modelo Secundário do Programa - Quantidade de dígitos!
Contagem = 1
while N >= 10: #Enquanto existir pelo menos dois dígitos, retiramos o dígito da direita e contamos + 1.
    N = N // 10
    Contagem += 1 #Segunda forma: Contagem = Contagem + 1
print('A quantidade de dígitos é:',Contagem)
