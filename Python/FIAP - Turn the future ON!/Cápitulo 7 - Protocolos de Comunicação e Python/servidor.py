# Preparação do servidor.
'''
Primeiramente, importamos todas (*) as funções da biblioteca “socket”,
isso será preciso para que possamos criar objetos do tipo “socket”.
'''
from socket import *

'''
Criamos duas variáveis, “servidor” e “porta”, para armazenarmos esses dois dados que serão
utilizados posteriormente; em “servidor”, poderíamos utilizar também a palavra “localhost”
para identificarmos que o servidor é a própria máquina que está executando o código, o que
também é representado pelo endereço “127.0.0.1”, que foi aqui utilizado. 
Em “porta”, escolhemos uma porta representada por um número inteiro entre 0 e 65535, em que
normalmente as portas entre 0 e 1023 são portas utilizadas, por padrão, para atribuições de
serviços conhecidos por meio do sistema operacional.
'''
servidor = "127.0.0.1"
porta = 43210

'''
Criamos o nosso objeto socket “obj_socket”, por meio da função “socket()”, que exige dois
parâmetros: o primeiro definirá a família responsável por identificar os pacotes. 
Para o nosso exemplo, definimos como AF_INET, o que significa que iremos utilizar a 
identificação do emissor/receptor do(s) pacote(s) via DNS ou número IP 
(poderíamos utilizar a constante AF_UNIX, o que mudaria a forma de identificar a 
origem/destino do(s) pacote(s)). Já o segundo parâmetro refere-se ao transporte desse pacote,
que pode ser SOCK_STREAM, que representa o protocolo TCP (o que nós optamos) ou SOCK_DGRAM,
que representa o protocolo de transporte UDP.
'''

obj_socket = socket(AF_INET, SOCK_STREAM)
# Fazendo a associação no nosso objeto socket com o nosso servidor e porta.
obj_socket.bind((servidor, porta))
# Definindo o máximo de clientes que o nosso servidor irá atender simultaneamente.
obj_socket.listen(2)
print("Aguardando cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print(f"Conectado com: {cliente}")
    while True:
        mensagem_enviada = str(conexao.recv(1024))
        print(f"Recebemos: {mensagem_enviada}")[2:-1]
        # Mensagem em forma bytes "b".
        mensagem_enviada = bytes(input("Sua resposta: "), 'utf-8')
        conexao.send(mensagem_enviada)
        break
    conexao.close()
