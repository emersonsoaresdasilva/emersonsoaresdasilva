# Arduino e o lado do Python.
import serial
"""
Começaremos pela biblioteca “serial”, que será a responsável por realizar a troca de dados entre o Arduino e o Python
por meio de uma comunicação que irá se estabelecer através de uma porta serial.

pip install pyserial
"""
conexao = ""
for porta in range(10):  # Percorre até o número da porta... caso a porta seja 0 <= 9.
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print(f"Conectado na porta: {conexao.portstr}")
        break
    except serial.SerialException:  # Exceção do tipo “serial.SerialException”, ou seja, a conexão não ocorreu.
        pass
if conexao != "":
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")
