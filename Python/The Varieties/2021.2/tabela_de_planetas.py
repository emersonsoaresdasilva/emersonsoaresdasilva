# Início →

# pip install tabulate
# pip install termcolor

from tabulate import tabulate
from termcolor import colored

def criar_cabecalho():
    cabecalho = ['Planeta', 'Raio (km)', 'Massa (x 10^21 kg)']
    return [colored(c, 'cyan', attrs=['bold']) for c in cabecalho]

def criar_tabela():
    tabela = [
        ['Sol', 696000, 198910000],
        ['Mercúrio', 2439, 330],
        ['Vênus', 6051, 641],
        ['Terra', 6371, 5973.6],
        ['Marte', 3390, 641.85],
        ['Júpiter', 69911, 1898600],
        ['Saturno', 58232, 568460],
        ['Urano', 25362, 86832],
        ['Netuno', 24622, 102430],
    ]
    return [[colored(d[0], 'yellow', attrs=['bold']), d[1], d[2]] for d in tabela]

print(tabulate(criar_tabela(), headers=criar_cabecalho(), tablefmt='fancy_grid'))
# ← Fim