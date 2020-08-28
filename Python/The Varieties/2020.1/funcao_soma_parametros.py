#Função Soma com parâmetros!
def soma(Numero1, Numero2):
    Resultado = Numero1 + Numero2
    print('Resultado:',Resultado)
    return

#Pedindo o valor (não declarado) para o usuário.
Numero1 = int(input('Digite o primeiro número: '))
Numero2 = int(input('Digite o último número: '))

#Chamando a função
soma(Numero1,Numero2)
