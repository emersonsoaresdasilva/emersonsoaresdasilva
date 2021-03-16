import unittest

'''
EXPLICACAO
    Uma pilha é uma estrutura de dados que tem um "topo".

    Ela armazena quantos elementos quisermos, mas só podemos retirar
    o elemento do topo.
    Quando adicionamos um elemento, só podemos adicionar no topo.

    Em inglês, diriamos Last In First Out, ou LIFO.

    Em uma pilha a operação "colocar no topo" é chamada de "push",
    e a operação "tirar do topo" é chamada de "pop".

    Em python, podemos implementar o conceito de pilha usando uma lista,
    que têm as funções append e pop

    EXEMPLO:

    pilha = []          # começamos com uma pilha vazia
    pilha.append(5)     # pilha: [5]
    pilha.append(8)     # pilha: [5, 8]
    pilha.append(4)     # pilha: [5, 8, 4]
    pilha.append(3)     # pilha: [5, 8, 4, 3]
    item = pilha.pop()  # pilha: [5, 8, 4]          desempilhou o 3
    item = pilha.pop()  # pilha: [5, 8]             desempilhou o 4
'''

'''
EXERCICIO 1
    Crie a função empilhar, que recebe uma pilha e um elemento
    e coloca o elemento no topo da pilha
'''

def empilhar(pilha, elemento):
    pilha.append(elemento)

'''
EXERCICIO 2
    Crie a função desempilhar, que recebe uma pilha, tira o elemento
    que estava no topo da pilha e retorna ele

    Exemplo:
    Se a pilha era [1, 2, 3], a pilha deve ficar sendo [1, 2] e a função
    deve retornar 3
'''

def desempilhar(pilha):
    item = pilha.pop()
    return item
    # return pilha.pop(-1)

'''
EXERCICIO 3
    Faça a função pilha_vazia que retorna verifica se a pilha está vazia.
    Deve retornar True se a pilha está vazia e False se não está
'''

def pilha_vazia(pilha):
    if pilha == []:
        return True
    return False

'''
EXERCICIO 4
    Faça uma função pilha_letras, que recebe uma string e vai colocando as
    letras da string uma a uma em uma pilha.
    Sua função deve retornar a pilha pronta.
    Exemplo:
    texto = "exemplo"
    pilha = ['e','x','e','m','p','l','o']
'''

def pilha_letras(texto):
    '''
    lista = list(texto)
    pilha = []
    for i in range(len(lista)):
        pilha.append(lista[i])
    return pilha
    '''
    return list(texto)

'''
EXERCICIO 5
    Fazer uma função "menos_o_d". Ela recebe uma string e vai colocando as
    letras uma a uma em uma pilha, como a funcao acima. Porém, quando ela
    vê uma letra d, ao invés de colocar o d, ela faz um pop() na pilha,
    tirando a ultima letra logo antes do d.

    Observe que se a primeira letra for d, ela talvez tente tirar uma coisa de
    uma pilha vazia.
    Outro caso ruim seria a string 'addd', que empilha um a, depois tira,
    depois tenta tirar de novo (3 vezes!)
    Nesses casos ruins, faça o seguinte: se a pilha está vazia e veio um "d",
    simplesmente não tire nada da pilha. Ela continuará vazia.

    Sua função deve retornar a ultima pilha.

    Exemplos:
    texto = "bandanad"
    pilha = ['b','a','a','n']

    texto = "abcdd"
    pilha = ['a']

    texto = "abdddc"
    pilha = [c]

    texto = "addd"
    pilha = []
'''

# Pilha primeiro elemento
# Fila ultimo elemento

def menos_o_d(texto):
    pilha = []
    for letra in texto:
        if letra == 'd':
            if not pilha_vazia(pilha):
                desempilhar(pilha)
        else:
            empilhar(pilha, letra)
    return pilha
'''
EXERCICIO 6
    Implemente a função 'verificar_balanceamento', que recebe como entrada
    uma string representando uma expressão aritmética contendo parenteses
    e verifica se os parênteses estão balanceados.

    Exemplo:
    - A expressao "(())"                está balanceada
    - A expressão "(((2+3)/5) - 1)"     está balanceada
    - A expressão "(((2+3)) - 1)"       está balanceada
    - A expressão "(((2+3) - 1)"        não está balanceada
    - A expressão "10 / (4 - 1) * (5))" não está balanceada

    Deve ser utilizada uma estrutura de Pilha para resolver o problema.

    Se a expressão estiver balanceada, deve retornar True,
    caso contrário deve retornar False
'''

def verificar_balanceamento(string):
    '''
    pilha = pilha_letras(string)
    abriu, fechou = 0,0

    for i in range(len(pilha)):
        if pilha[i] == ')':
            fechou += 1
        elif pilha[i] == '(':
            abriu += 1

    if abriu == fechou:
        if pilha[0] != ')':
            return True
        return False
    '''
    pilha = []
    for i in string:
        if i == '(':
            empilhar(pilha, i)
        elif i == ')':
            if pilha_vazia(pilha):
                return False
            desempilhar(pilha)
    return pilha_vazia(pilha)

# ------------------------------------------------------------
'''
O trecho de código abaixo não deve ser alterado.
Ele irá testar a implementação do seu código ao executar o arquivo
'''


class TestStringMethods(unittest.TestCase):

    def test_01_empilhar(self):
        pilha_teste1 = [2, 3]
        empilhar(pilha_teste1, 4)
        self.assertEqual(pilha_teste1, [2, 3, 4])
        empilhar(pilha_teste1, 5)
        self.assertEqual(pilha_teste1, [2, 3, 4, 5])
        pilha_teste2 = []
        empilhar(pilha_teste2, 5)
        self.assertEqual(pilha_teste2, [5])

    def test_02_desempilhar(self):
        pilha_teste3 = [1, 2, 3, 4, 5, 6, 7]
        topo = desempilhar(pilha_teste3)
        self.assertEqual(topo, 7)
        self.assertEqual(pilha_teste3, [1, 2, 3, 4, 5, 6])
        topo = desempilhar(pilha_teste3)
        self.assertEqual(topo, 6)
        self.assertEqual(pilha_teste3, [1, 2, 3, 4, 5])
        topo = desempilhar(pilha_teste3)
        self.assertEqual(topo, 5)
        self.assertEqual(pilha_teste3, [1, 2, 3, 4])

    def test_03_pilha_vazia(self):
        pilha_teste4 = [1, 2, 3]
        vazia = []
        self.assertTrue(pilha_vazia(vazia))
        self.assertFalse(pilha_vazia(pilha_teste4))

    def test_04_pilha_letras(self):
        pilha = pilha_letras('banana')
        correto = ['b', 'a', 'n', 'a', 'n', 'a']
        self.assertEqual(pilha, correto)

    def test_05_menos_o_d(self):
        pilha = menos_o_d('banana')
        correto = ['b', 'a', 'n', 'a', 'n', 'a']
        self.assertEqual(pilha, correto)
        pilha = menos_o_d('bandana')
        correto = ['b', 'a', 'a', 'n', 'a']
        self.assertEqual(pilha, correto)
        pilha = menos_o_d('addd')
        correto = []
        self.assertEqual(pilha, correto)
        pilha = menos_o_d('dbandana')
        correto = ['b', 'a', 'a', 'n', 'a']
        self.assertEqual(pilha, correto)

    def test_06_verificar_balanceamento(self):
        expressao = '(1)'
        self.assertTrue(verificar_balanceamento(expressao))
        expressao = '(((2+3)/5) - 1)'
        self.assertTrue(verificar_balanceamento(expressao))
        expressao = '((((((((((()))))))))))'
        self.assertTrue(verificar_balanceamento(expressao))
        expressao = '(((()(((7+3)))))())'
        self.assertTrue(verificar_balanceamento(expressao))
        expressao = '10 / (4 - 1) * (5))'
        self.assertFalse(verificar_balanceamento(expressao))
        expressao = '(((())))))'
        self.assertFalse(verificar_balanceamento(expressao))
        expressao = '((((())))'
        self.assertFalse(verificar_balanceamento(expressao))
        expressao = '))(('
        self.assertFalse(verificar_balanceamento(expressao))
        expressao = ')((()))('
        self.assertFalse(verificar_balanceamento(expressao))


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=False).run(suite)


runTests()
