# Identificando as portas da nossa máquina que estão sendo utilizadas para serviços.
import socket

print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("ftp"))

'''
Com a execução desse código, teremos o retorno das portas que estamos disponibilizando para:
• Domínio (por padrão 53), usado para resolver a conversão entre DNS e IP;
• HTTP (por padrão 80), usado para navegar nas páginas WEB;
• FTP (por padrão 21), usado para transferência de arquivos.
'''
