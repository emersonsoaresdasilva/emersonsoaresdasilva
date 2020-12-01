import os
from ftplib import *

ftp_ativo = False
ftp = FTP(input("Digite o FTP que deseja conectar: "))
print(ftp.getwelcome())
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print(
    f"\n"
    f"Conexão bem sucedida.\"\n"
    f"Diretório atual de trabalho: {ftp.pwd()}\n")
menu = "1"
while menu == "1" or menu == "2" or menu == "3":
    menu = input(
        "\n"
        "<1> - para listar arquivos.\n"
        "<2> - para definir um diretório.\n"
        "<3> - para baixar um arquivo.       \n"
        "        \n"
        "Escolha a opção desejada: ")
    if menu == "1":
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print(f"\nDiretório corrente é: {ftp.pwd()}")
    elif menu == "3":
        tipo = input("Digite <B> para arquivo binário ou qualquer outra letra para arquvio ASCII: ").upper()
        if tipo == "B":
            with open(input("Digite o nome do arquivo destino: "), "wb") as arquivo:
                ftp.retrbinary("RETR " + input("Arquivo de origem: "), arquivo.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), "w") as arquivo:
                def escreverLinha(data):
                    arquivo.write(data)
                    arquivo.write(os.linesep)


                ftp.retrlines("RETR " + input("Arquivo de origem:"), escreverLinha)
            print("Arquivo baixado com sucesso!\n")
ftp.quit()
