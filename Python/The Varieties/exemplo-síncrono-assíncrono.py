# =========================================================================#
#                           INTRODUÇÃO
#                    Profº Jorge Pretel (Youtube)
# =========================================================================#

'''
A diferença entre síncrono e assíncrono.

• Síncrono = Rua de mão única.

- Quando precisamos aguardar, quando executamos uma função, ele deverá ser executado linha a linha.

- É necessário aguardar o termino de uma execução para iniciar uma nova execução.

• Assíncrono = Rua de uma ou mais faixas.

- Podemos executar diversas tarefas em paralelo, ou seja não precisamos aguardar o termino da primeira execução.
'''
# =========================================================================#
#                               SÍNCRONO
# =========================================================================#
'''
import time

def print_name(position, name):
    time.sleep(1)
    print(f'{position} - {name}')

start_time = time.time()

print_name('1', 'Pedro')
print_name('2', 'Lucas')
print_name('3', 'Luciano')

end_time = time.time()
total_time = 1000*(end_time-start_time)
print(f'Total time = {total_time:.2f} ms') #Tempo de execução do script.
'''
# =========================================================================#
#                   EXEMPLO BACKUP SERVIDORES - SÍNCRONO
# =========================================================================#
'''
import time
#Criando uma lista de servidores.
servers = [f'192.168.0.{ip}'for ip in range(11,32)]

def simulation_ssh_connection(posiotion, ip):
    print(f'{position} - {ip}')

start_time = time.time()

for position, ip in enumerate(servers): #Para cada servidor em severs, será chamada a função "simulation_ssh_connection".
    time.sleep(0.5)
    simulation_ssh_connection(position, ip)

end_time = time.time()
total_time = 1000*(end_time - start_time)
print(f'Total time = {total_time:.2f} ms') #Tempo de execução do script.
'''
# =========================================================================#
#                   TRATANDO SOMENTE OS DADOS DESEJADOS.
# =========================================================================#
'''
import time
import asyncio #Permite a passagem para execução de outra função.

#Criando uma lista de servidores.
servers = [f'192.168.0.{ip}' for ip in range(11,32)]

total_servers = int(len(servers))/10+1
count = 0
while count < total_servers:
    for server in servers:
        my_new_server = servers[:10] #Pegando de 0 a 10 os indices da lista.
        for my_server in my_new_server: 
            print(my_server) #Imprimo todos os servers.
        print()
        del servers[:10] #Deletando os 10 primeiros da lista.
        print(my_new_server)
        count += 1      
'''
# =========================================================================#
#               EXEMPLO BACKUP SERVIDORES - ASSÍNCRONO + RÁPIDO
# =========================================================================#
'''
import time
import asyncio #Permite a passagem para execução de outra função.

#Criando uma lista de servidores.
servers = [f'192.168.0.{ip}' for ip in range(11,32)]

async def simulation_ssh_connection(position, ip): #Essa função permite que ela seja parada para outra função ser executada.
    #Coneca via SSH.
    await asyncio.sleep(1) #Permite a execução de outro servidor.
    print(f'{position} - {ip}') #Imprime o nome do servidor.

start_time = time.time()

loop = asyncio.get_event_loop()
tasks = [simulation_ssh_connection(position, ip) for position, ip in enumerate(servers)]#Tarefas que serão executadas.
#Enumerate: retorna a numeração do objeto, pega uma lista e retornar uma tupla.

#Executa esse loop aqui e não espera completar.
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
total_time = 1000*(end_time - start_time)
print(f'Total time = {total_time:.2f} ms') #Tempo de execução do script.
'''
