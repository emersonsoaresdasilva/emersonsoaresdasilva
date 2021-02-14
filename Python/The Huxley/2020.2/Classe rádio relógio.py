# Implemente a classe RadioRelogio com os atributos e metodos, seguindo as especificacoes do problema:
class RadioRelogio:

    def __init__(self):
        self.__hora = 0
        self.__minuto = 0
        self.__frequencia_am = 530
        self.__frequencia_fm = 879
        self.__banda = 'FM'

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_frequencia(self):
        if self.__banda == 'AM':
            return self.__frequencia_am
        else:
            return self.__frequencia_fm

    def get_banda(self):
        return self.__banda

    def set_hora(self, hora):
        if hora < 0 or hora > 23:
            hora = 0
        self.__hora = hora

    def set_minuto(self, minuto):
        if minuto < 0 or minuto > 59:
            minuto = 0
        self.__minuto = minuto

    def set_banda(self, banda):
        if banda != 'AM':
            banda = 'FM'
        else:
            banda = 'AM'
        self.__banda = banda

    def tick(self):
        self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
            if self.__hora > 23:
                self.__hora = 0

    def aumentar_frequencia(self):
        if self.__banda == 'AM':
            self.__frequencia_am += 10
            if self.__frequencia_am > 1700:
                self.__frequencia_am = 530
        else:
            self.__frequencia_fm += 2
            if self.__frequencia_fm > 1079:
                self.__frequencia_fm = 879

    def diminuir_frequencia(self):
        if self.__banda == 'AM':
            self.__frequencia_am -= 10
            if self.__frequencia_am < 530:
                self.__frequencia_am = 1700
        else:
            self.__frequencia_fm -= 2
            if self.__frequencia_fm < 879:
                self.__frequencia_fm = 1079


"""
  O codigo abaixo serve apenas para testar a sua classe.
  Voce nao precisa se preocupar com ele e nem com os detalhes tecnicos utilizados a partir deste ponto.
"""
def testa_atividade(nome_teste, valor=None):
	if nome_teste == 'existe classe':
		try:
			aparelho = RadioRelogio()
			print('Classe definida')
		except:
			print('Classe inexistente')
	else:
		aparelho = RadioRelogio()
		if nome_teste == 'existe hora':
			valor = aparelho._RadioRelogio__hora
			print(valor)
		elif nome_teste == 'existe minuto':
			valor = aparelho._RadioRelogio__minuto
			print(valor)
		elif nome_teste == 'existe frequencia_am':
			valor = aparelho._RadioRelogio__frequencia_am
			print(valor)
		elif nome_teste == 'existe frequencia_fm':
			valor = aparelho._RadioRelogio__frequencia_fm
			print(valor)
		elif nome_teste == 'existe banda':
			valor = aparelho._RadioRelogio__banda
			print(valor)
		elif nome_teste == 'testa get_hora()':
			aparelho._RadioRelogio__hora = valor['hora']
			print(aparelho.get_hora())
		elif nome_teste == 'testa get_minuto()':
			aparelho._RadioRelogio__minuto = valor['minuto']
			print(aparelho.get_minuto())
		elif nome_teste == 'testa get_frequencia()':
			if valor['banda'] == 'AM':
				aparelho._RadioRelogio__frequencia_am = valor['frequencia']
			else:
				aparelho._RadioRelogio__frequencia_fm = valor['frequencia']
			aparelho._RadioRelogio__banda = valor['banda']
			print(aparelho.get_frequencia())
		elif nome_teste == 'testa get_banda()':
			aparelho._RadioRelogio__banda = valor['banda']
			print(aparelho.get_banda())
		elif nome_teste == 'testa set_hora()':
			aparelho.set_hora(valor['hora'])
			print(aparelho._RadioRelogio__hora)
		elif nome_teste == 'testa set_minuto()':
			aparelho.set_minuto(valor['minuto'])
			print(aparelho._RadioRelogio__minuto)
		elif nome_teste == 'testa set_banda()':
			aparelho.set_banda(valor['banda'])
			print(aparelho._RadioRelogio__banda)
		elif nome_teste == 'testa tick()':
			aparelho._RadioRelogio__hora = valor['hora']
			aparelho._RadioRelogio__minuto = valor['minuto']
			aparelho.tick()
			print('{0:02d}:{1:02d}'.format(aparelho._RadioRelogio__hora, aparelho._RadioRelogio__minuto))
		elif nome_teste == 'testa aumentar_frequencia()':
			aparelho._RadioRelogio__banda = valor['banda']
			for i in range(valor['repeticoes']):
				aparelho.aumentar_frequencia()
			if valor['banda'] == 'AM':
				print(aparelho._RadioRelogio__frequencia_am)
			else:
				print(aparelho._RadioRelogio__frequencia_fm)
		elif nome_teste == 'testa diminuir_frequencia()':
			aparelho._RadioRelogio__banda = valor['banda']
			if valor['banda'] == 'AM':
				aparelho._RadioRelogio__frequencia_am = valor['freq_inicial']
			else:
				aparelho._RadioRelogio__frequencia_fm = valor['freq_inicial']
			for i in range(valor['repeticoes']):
				aparelho.diminuir_frequencia()
			if valor['banda'] == 'AM':
				print(aparelho._RadioRelogio__frequencia_am)
			else:
				print(aparelho._RadioRelogio__frequencia_fm)

def main():
	nome_teste = input()
	valor = eval(input())
	testa_atividade(nome_teste, valor)
main()
