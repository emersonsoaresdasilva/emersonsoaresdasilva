# Persistindo os dados recolhidos.
import json
import time
import serial
from datetime import datetime

conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200)
        print(f"Conectado na porta: {conexao.portstr}")
        break
    except serial.SerialException:
        pass
if conexao != "":
    dicionario = {}  # Criamos um dicionário para armazenar os dados no arquivo json.
    contador = 0
    while contador < 10:
        resposta = conexao.readline()
        """
        Iremos adicionar no “dicionario” um novo elemento que terá como chave a data e hora (now() retorna,
        data e hora com milissegundo) e o valor será o dado retornado por meio da porta serial,
        decodificado para string e consideraremos apenas os três primeiros caracteres ([0:3]),
        que representam efetivamente o nível de luminosidade. Por exemplo: {"2018-06-16 20:33:14.022459": ["958"]}.
        """
        dicionario[str(datetime.now())] = [resposta.decode("utf-8")[0:3]]
        print(resposta.decode())
        contador += 1
    with open("Temperatura.json", "w") as arquivo_json:
        json.dump(dicionario, arquivo_json)  # Realizando a gravação dos dados no arquivo json.
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")
