'''
Crie um programa que receba como entrada o valor total de uma dívida
(número natural maior que zero) e o valor máximo que o devedor pode
pagar todo mês (número natural maior que zero). O programa deve
exibir o restante da dívida antes e depois de cada pagamento
mensal até que a dívida zere.
Obs.: quando a dívida é menor do que o máximo que o devedor
pode pagar, ele pagará exatamente quanto deve,
jamais pagará um valor superior.

Formato de entrada
Na primeira linha um valor natural maior que zero indicando o valor
da dívida;
na segunda linha o valor máximo que o devedor pode pagar por mês
(novamente um valor natural maior que zero).

Formato de saída
O valor da dívida restante antes do pagamento mensal
e o valor da dívida restante depois do pagamento mensal,
conforme o formato nos exemplos.
'''
Valor_divida = int(input())
Valor_mensal = int(input())

while(Valor_divida > 0): #Enquanto o valor da dívida for > 0
    print('(antes)',Valor_divida) #Imprime valor dívida, antes do pagamento.
    Valor_divida = Valor_divida - Valor_mensal #Cálcula valor dívida - Valor pagamento.
    if Valor_divida <= 0: #Se o valor da dívida for < 0, ele atribui 0 para valor da dívida.
        Valor_divida = 0 #Se não "Sem else" ele retorna ao laço até que o valor da dívida seja <= 0.
    print('(depois)',Valor_divida) #Imprime valor dívida, após os pagamentos.
        

