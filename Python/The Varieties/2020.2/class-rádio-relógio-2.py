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
