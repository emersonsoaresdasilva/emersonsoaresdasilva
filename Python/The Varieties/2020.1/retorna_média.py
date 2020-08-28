# Objetivo: Calcular a média aritmética de três números.
# Entrada.: Três números inteiros.
# Saída...: A média aritmética dos números lidos.
# Função de boas-vindas ao usuário.

def bem_vindo():
    print('Bem-vindo! Vamos calcular a média')
    
# Função que calcula e exibe a média aritmética de três números.
def retorna_media(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma / 3

# Programa principal.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Dá boas-vindas ao usuário.
bem_vindo()

# Executa a função de média e armazena o valor retornado.
resposta = retorna_media(a, b, c)

# Exibindo a resposta da função.
print('A média é %.2f' % (resposta))
