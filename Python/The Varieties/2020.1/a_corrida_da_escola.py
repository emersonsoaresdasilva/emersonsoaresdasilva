'''
A escola de Joãozinho tradicionalmente organiza uma corrida ao redor do prédio. Como todos os alunos são
convidados a participar e eles estudam em períodos diferentes, é difícil que todos corram ao mesmo tempo.

Para contornar esse problema, os professores cronometram o tempo que cada aluno demora para dar cada volta
ao redor da escola, e depois comparam os tempos para descobrir a classificação final.

Sua tarefa é, sabendo o número de competidores, o número de voltas de que consistiu a corrida e os tempos
de cada aluno competidor, descobrir quem foi o aluno vencedor, para que ele possa receber uma medalha
comemorativa.

Entrada:

A primeira linha da entrada contém dois inteiros N e M representando o número de competidores e o número
de voltas da corrida, respectivamente.

Cada uma das N linhas seguintes representa um competidor: a primeira linha representa o primeiro competidor,
a segunda linha representa o segundo competidor, e assim por diante. Cada linha contém M inteiros
representando os tempos em cada volta da corrida: o primeiro inteiro é o tempo da primeira volta, o segundo
inteiro é o tempo da segunda volta, e assim por diante.

Garante-se que não houve dois competidores que gastaram o mesmo tempo para completar a corrida inteira.

Considere:

• 2 <= N <= 100
• 1 <= M <= 100
• 1 <= qualquer número da entrada que represente o tempo de uma volta <= 1000000

Exemplo:

2 3
5 1 2
7 2 5

Saída:

A saída consiste de um único inteiro, que corresponde ao número do competidor que ganhou a corrida.

Exemplo: 1
'''
'''
n = input().split()
m = int(n[0])
competidores = []

for c in range(m):
    linha = input().split()
    total = 0
    for x in linha:
        x = int(x)
        total += x
    competidores.append((total, c+1))
competidores.sort()
print(competidores[0][1])
'''
#---------------------------------------
#      VERSÃO PROGRAMA PROFESSOR
#---------------------------------------
def converter(lista):
    for indice in range(len(lista)):
        lista[indice] = int(lista[indice])
    return lista

def soma(lista):
    soma = 0
    for indice in range(len(lista)):
        soma += lista[indice]
    return soma

N, M = input().split()

N = int(N)
M = int(M)
menor = 1000000 * 101

for i in range(1, N+1): #Iniciando o i em 1.
    voltas = input().split()
    voltas = converter(voltas) #Função converter recebe lista com strings e converter para inteiros.
    total = sum(voltas)
    if total < menor:
        menor = total
        competidor = i
print(competidor)
















