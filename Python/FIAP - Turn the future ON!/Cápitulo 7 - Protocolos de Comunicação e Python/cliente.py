# Preparação do cliente.
from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

'''
Observe que utilizamos a função “bytes()” para converter o conteúdo do input, ou seja,
a string para o formato bytes, mais uma vez, lembrando: o socket transmite somente dados
do tipo byte. 
A função “bytes()” possui o segundo parâmetro que faz referência ao padrão de caracteres “utf-8”.
'''

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    '''
    Conexão com o servidor, por meio da função “connect()”, e, finalmente, enviando uma mensagem
    para o servidor, utilizando o método “send()”.
    '''
    obj_socket.connect((servidor, porta))
    mensagem = bytes(input("Digite algo: "), "utf-8")
    obj_socket.send(mensagem)
    resposta = obj_socket.recv(1024)
    # A variável resposta recebe o dado enviado pelo servidor, limitando o tamanho para 1024 bytes.
    print(f"Resposta do Servidor: {resposta}")[2:-1]
    if str(resposta)[2:-1].upper() == "FIM":
        break
obj_socket.close()
