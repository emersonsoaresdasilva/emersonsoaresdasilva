from socket import *

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connet((servidor, porta))
saida = None
while saida != "X":
    mensagem = input("Sua mensagem: ")
    obj_socket.sendto(mensagem.endcode(), (servidor, porta))
    """
    “sendto()” possui dois parâmetros: a mensagem e o destino da mensagem. 
    """
    dados, origem = obj_socket.recvfrom(65535)
    print(f"Resposta do Servidor: {dados.encode()}")
    saida = input("Digite <X> para sair: ").upper()
obj_socket.close()git