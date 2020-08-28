'''Crie um programa que exiba horas, minutos e segundos de um relógio,
considerando de 00:00:00 até 23:59:59.'''

'''
while True:
    for relogio in range(60): #[0...60[
        print(relogio, end= ' ')
'''
'''
for minuto in range(3):
    for segundo in range(60): # [0...60[
        print(segundo, end=' ')
'''

from time import sleep
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60): # [0...60[
            print('%02d:%02d:%02d'%(hora,minuto,segundo))
            sleep(1)

