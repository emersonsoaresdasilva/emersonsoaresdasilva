#As tuplas são estruturas também para dados voláteis, assim como as variáveis, listas e dicionários.
'''
Uma característica única das tuplas é o fato de elas não aceitarem alteração sobre os dados que já estiverem nelas inseridos.

Além disso, as tuplas sempre são representadas com seus dados entre parênteses.

Aplicamos mais o conceito de tuplas para realizar a leitura de uma resposta do Python, e não de alguém que inseriu dados.
'''

#Curiosidade (Octetos):
'''
São as divisões que formam um endereço IP.
Por exemplo, no endereço IP 172.168.5.2 teremos 4 octetos, que também podem ser chamados de byte,
uma vez que um byte é formado por 8 bits (daí octeto).
'''

ips = {}
resposta = "S"

while resposta == "S":
    ips[(input("Digite os dois octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resposta = input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")

for ip in ips.keys():
    print(ip[0]+'.'+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ")

for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1] == pesquisa):
        print(nome)

print("Exibindo as máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")

for ip, nome in ips.items():
    if(ip[0] == rede):
        print(nome)
