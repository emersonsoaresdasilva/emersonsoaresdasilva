"""
Começamos importando e estabelecendo o endereço do servidor
e a porta que será utilizada para a comunicação.
"""
from socket import *
"""
Na terceira linha, alteramos o segundo parâmetro para DGRAM,
o que determina que utilizaremos o protocolo de transporte UDP.
"""
servidor = "127.0.0.1"
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))  # Realizamos o bind do servidor com a porta e endereço especificados.

print("Servidor pronto...")
while True:
    dados, origem = obj_socket.recvfrom(65535)
    print(f"Origem..............: {origem}")
    print("Dados recebidos.....:", dados.decode())
    """
    Perceba que agora não utilizamos mais a conversão para string e o slice,
    em vez disso, usamos a função “decode()”, que exibe os dados bytes no formato string.
    """
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)
    """
    Recebemos a resposta que o servidor deseja passar e encaminhamos para o cliente por meio do método
    “sendto()”, que é formado por dois parâmetros: o primeiro é a mensagem propriamente dita,
    na qual, dessa vez, utilizamos o método encode() para converter de string para byte;
    e o segundo parâmetro é a origem para a qual desejamos enviar a mensagem.
    """
obj_socket.close()
