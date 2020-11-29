# Protocolo de comunicação e Python.
# Tudo começa com a biblioteca "Socket".

# Vejamos um primeiro exemplo para recuperarmos o endereço IP por meio do DNS:
import socket

resposta = "S"

while resposta == "S":
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)  # Recebe uma URL e retorna o IP.
    print(f"O IP referente à url informada é: {ip}")
    resposta = input("Digite <S> para continuar: ").upper()
