from ftplib import *

ftp = FTP("ftp.ibiblio.org")
print(ftp.getwelcome())
ftp.login()
ftp.cwd("/pub/linux/logos/pictures")
with open("pai_do_linux.jpg", "wb") as arquivo:
    ftp.retrbinary("RETR linus-father-of-linux.jpg", arquivo.write)
    # Devemos especificar o retorno (RETR) e o nome do arquivo que será retornado. ("RETR ...")
ftp.quit()
