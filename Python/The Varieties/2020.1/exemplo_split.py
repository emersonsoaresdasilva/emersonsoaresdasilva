''' Crie um programa que faça a leitura de quatro valores inteiros dados pelo
usuário.
O programa deverá exibir a soma dos quatro valores lidos.
Observação: Os quatro valores estão na mesma linha e separados por espaço.'''

N1, N2, N3, N4 = input().split()

N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
N4 = int(N4)

SOMA = N1 + N2 + N3 + N4

print(SOMA)
