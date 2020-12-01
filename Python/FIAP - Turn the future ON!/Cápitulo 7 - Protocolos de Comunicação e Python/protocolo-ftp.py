# O mundo não é feito só de sockets.
from ftplib import *

"""
O método FTP(), que precisa apenas do endereço do servidor FTP, no exemplo,
utilizamos o endereço “ftp.ibiblio.org”. 
Caso queira, pode acessá-lo diretamente em seu browser, 
por meio do endereço “ftp://ftp.ibiblio.org/”, irá surgir uma imagem como a que será
apresentada logo a seguir.
"""
ftp = FTP("ftp.ibiblio.org")
"""
O método getwelcome() do objeto “ftp”, que irá apresentar uma mensagem-padrão retornada pelo servidor.
Essa mensagem pode, por exemplo, ser útil para informar ao cliente que algum arquivo está indisponível,
ou que o servidor está passando por uma atualização, ou simplesmente ser responsável por um “olá”.
"""
print(ftp.getwelcome())
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("Diretório atual de trabalho: ", ftp.pwd())  # pwd() retorna o endereço atual de trabalho.
ftp.cwd("pub")  # cwd() deslocando-se entre os diretórios.
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))  # Lista de arquivo encontrados no diretório atual.
ftp.quit()