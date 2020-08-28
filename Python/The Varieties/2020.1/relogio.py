'''Crie um programa que exiba hh:mm:ss de um relógio,
considerando de 00:00:00 até 23:59:59.'''

from time import sleep

for h in range(24):
    for m in range(60):  # [0..60[
        for s in range(60): # [0..60[
            print('\n' * 20)
            print('%02d:%02d:%02d' % (h, m, s))
            sleep(0.001)

