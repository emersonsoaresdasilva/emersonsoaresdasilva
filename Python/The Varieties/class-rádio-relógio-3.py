
'''
• A partir das classes:
    • Radio: implementa as funcionalidades básicas de um rádio.
    • Relogio: implementa as funcionalidades básicas de um relógio.
• Podemos criar uma classe chamada RadioRelogio, utilizando herança múltipla.
'''

# Definição da classe Radio.
class Radio:
    def __init__(self, banda, frequencia_am, frequencia_fm):
        self.banda = banda
        self.frequencia_am = frequencia_am
        self.frequencia_fm = frequencia_fm

    def set_banda(self, banda):
        if banda not in ['AM', 'FM']:
            banda = 'AM'
        self.banda = banda

    def get_frequencia(self):
        if self.banda == 'AM':
            return self.frequencia_am
        return self.frequencia_fm

# Definição da classe Relogio

class Relogio:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def tick(self):
        self.minuto += 1
        if self.minuto > 59:
            self.minuto = 0
            self.hora += 1
            if self.hora > 23:
                self.hora = 0

'''
Classe RadioRelogio a partir das classe Radio e Relógio.
'''

# Definição da classe RadioRelogio (com heran ̧ca m ́ultipla a partir das classes Radio e Relogio)
class RadioRelogio(Radio, Relogio):
    def __init__(self, alarme_hora, alarme_minuto):
        Radio.__init__(self, 'FM', 530, 879)
        Relogio.__init__(self, 12, 0)
        self.alarme_hora = alarme_hora
        self.alarme_minuto = alarme_minuto
        self.alarme_ligado = False

    def tick(self):
        Relogio.tick(self)
        if self.hora == self.alarme_hora and self.minuto == self.alarme_minuto:
            self.alarme_ligado = True

    def desligar_alarme(self):
        self.alarme_ligado = False

#Programa Principal
rr = RadioRelogio(13, 45)
rr.hora = 13
rr.minuto = 44
print('Alarme ligado?', rr.alarme_ligado)
print('hora e minuto: %2d:%2d' % (rr.hora, rr.minuto))
print('Passando a hora...')
rr.tick()
print('hora e minuto: %2d:%2d' % (rr.hora, rr.minuto))
print('Alarme ligado?', rr.alarme_ligado)


#Exemplo de saida:

# Alarme ligado? False
# hora e minuto: 13:44
# Passando a hora...
# hora e minuto: 13:45
# alarme ligado? True
