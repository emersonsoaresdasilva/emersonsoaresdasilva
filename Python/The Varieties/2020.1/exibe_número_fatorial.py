#Faça um programa que calcule e exiba o fatorial de um número natural n fornecido pelo
#usuário (o fatorial de n escreve-se n!). O programa deverá conter a função fatorial(n) que
#devolve o fatorial de n, e não deve ser usado o módulo de matemática para isso. Dica: você
#pode usar a função factorial do módulo de matemática para testar se o resultado da sua
#função está correto!

#Exemplo: 5! = 5 · 4 · 3 · 2 · 1 · 0! = 120 , pois por definição 0! = 1 .

def fatorial(n):
    f = 1
    for i in range(1,n+1): #[1...n+1[
        f = f * i
    return f

n = int(input('n: '))
print('%d! = %d'%(n, fatorial(n)))
