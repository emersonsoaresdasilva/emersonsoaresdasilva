# Implemente abaixo as classes Funcionario, Vendedor e Gerente com os atributos e metodos, seguindo as especificacoes do problema:
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf, data_nasc, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_dia_nasc(self):
        return int(self.__data_nasc[:2])
    def get_mes_nasc(self):
        return int(self.__data_nasc[3:5])
    def get_ano_nasc(self):
        return int(self.__data_nasc[-4:])         
    def get_salario(self):
        return self.__salario

    def set_nome(self, nome):
        self.__nome = nome
    def set_cpf(self, cpf):
        self.__cpf = cpf
    def set_data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc
    def set_salario(self, salario):
        self.__salario = salario

    @abstractmethod
    def calcular_salario_final(self):
        pass
    @abstractmethod
    def converter_para_string(self):
        pass

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, data_nasc, salario, quantidade_vendas):
        Funcionario.__init__(self, nome, cpf, data_nasc, salario)
        self.__quantidade_vendas = quantidade_vendas

    def get_quantidade_vendas(self):
        return self.__quantidade_vendas

    def set_quantidade_vendas(self, quantidade_vendas):
        self.__quantidade_vendas = quantidade_vendas

    def calcular_salario_final(self):
        return self.get_salario() * (0.005 * self.__quantidade_vendas + 1)

    def converter_para_string(self):
        return f"{self.get_nome()};{self.get_cpf()};{str(self.get_ano_nasc())}-{str(self.get_mes_nasc())}-{str(self.get_dia_nasc())};{self.get_salario():.2f};{self.__quantidade_vendas}"

class Gerente(Funcionario):
    def __init__(self, nome, cpf, data_nasc, salario):
        Funcionario.__init__(self, nome, cpf, data_nasc, salario)
        self.__vendedores = []

    def adicionar_vendedor(self, vendedor):
        self.__vendedores.append(vendedor)

    def calcular_salario_final(self):
        vendas = 0
        for v in self.__vendedores:
          vendas += v.get_quantidade_vendas()
        return self.get_salario() * (0.001 * vendas + 1) 

    def converter_para_string(self):
        cpfs_vendedores = []
        for v in self.__vendedores:
          cpfs_vendedores.append(str(v.get_cpf()))
        
        return f"{self.get_nome()};{self.get_cpf()};{str(self.get_ano_nasc())}-{str(self.get_mes_nasc())}-{str(self.get_dia_nasc())};{self.get_salario():.2f};{','.join(cpfs_vendedores)}"

"""
  O codigo abaixo serve apenas para testar as suas classes.
  Voce nao precisa se preocupar com ele e nem com os detalhes tecnicos utilizados a partir deste ponto.
"""

class DummyFuncionario(Funcionario):
	def __init__(self, nome, cpf, data_nasc, salario):
		super().__init__(nome, cpf, data_nasc, salario)
	def calcular_salario_final(self, percentual):
		return 'resultado calcular_salario_final'
	def converter_para_string(self):
		return 'resultado converter_para_string'

def testa_metodos_abstratos(nome_metodo):
	ok = False
	try:
		f = Funcionario('', 0, '01/01/1970', 0.0)
	except TypeError as e:
		msg = ''
		if hasattr(e, 'message'):
			 msg = str(e.message)
		else:
			msg = str(e)
		if 'abstract method' in msg and nome_metodo in msg:
			print('OK')
			ok = True
	if not ok:
		print('Metodo nao abstrato ou inexistente')

def testa_atividade(nome_teste, valor=None):
	if nome_teste == 'existe classe':
		if valor['classe'] == 'Funcionario':
			try:
				teste = DummyFuncionario('Maria', 12345678910, '01/01/1970', 5000.0)
				if not isinstance(teste, Funcionario):
					raise Exception
				print('Classe correta')
			except:
				print('Classe incorreta')
		if valor['classe'] == 'Vendedor':
			try:
				teste = Vendedor('Maria', 12345678910, '01/01/1970', 5000.0, 3)
				if not isinstance(teste, Funcionario):
					raise Exception
				print('Classe correta')
			except:
				print('Classe incorreta')
		if valor['classe'] == 'Gerente':
			try:
				teste = Gerente('Maria', 12345678910, '01/01/1970', 5000.0)
				if not isinstance(teste, Funcionario):
					raise Exception
				print('Classe correta')
			except:
				print('Classe incorreta')
	else:
		func = None
		if valor['classe'] == 'Funcionario':
			func = DummyFuncionario(valor['nome'], valor['cpf'], valor['data_nasc'], valor['salario'])
		elif valor['classe'] == 'Vendedor':
			func = Vendedor(valor['nome'], valor['cpf'], valor['data_nasc'], valor['salario'], valor['quantidade_vendas'])
		elif valor['classe'] == 'Gerente':
			func = Gerente(valor['nome'], valor['cpf'], valor['data_nasc'], valor['salario'])
			if 'vendedores' in valor:
				for item in valor['vendedores']:
					func.adicionar_vendedor(item)
		if not isinstance(func, Funcionario):
			raise Exception('Heranca incorreta')
		if nome_teste == 'testa atributos':
			if valor['classe'] == 'Funcionario' and valor['atributo'] == 'nome':
				print(func._Funcionario__nome)
			elif valor['classe'] == 'Funcionario' and valor['atributo'] == 'cpf':
				print(func._Funcionario__cpf)
			elif valor['classe'] == 'Funcionario' and valor['atributo'] == 'data_nasc':
				print(func._Funcionario__data_nasc)
			elif valor['classe'] == 'Funcionario' and valor['atributo'] == 'salario':
				print(func._Funcionario__salario)
			elif valor['classe'] == 'Vendedor' and valor['atributo'] == 'quantidade_vendas':
				print(func._Vendedor__quantidade_vendas)
			elif valor['classe'] == 'Gerente' and valor['atributo'] == 'vendedores':
				print(type(func._Gerente__vendedores))
		elif nome_teste == 'testa metodos':
			if valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_nome':
				print(func.get_nome())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_cpf':
				print(func.get_cpf())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_dia_nasc':
				print(func.get_dia_nasc())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_mes_nasc':
				print(func.get_mes_nasc())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_ano_nasc':
				print(func.get_ano_nasc())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'get_salario':
				print(func.get_salario())
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'set_nome':
				func.set_nome(valor['novo_nome'])
				print(func._Funcionario__nome)
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'set_cpf':
				func.set_cpf(valor['novo_cpf'])
				print(func._Funcionario__cpf)
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'set_data_nasc':
				func.set_data_nasc(valor['novo_data_nasc'])
				print(func._Funcionario__data_nasc)
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'set_salario':
				func.set_salario(valor['novo_salario'])
				print(func._Funcionario__salario)
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'calcular_salario_final':
				testa_metodos_abstratos('calcular_salario_final')
			elif valor['classe'] == 'Funcionario' and valor['metodo'] == 'converter_para_string':
				testa_metodos_abstratos('converter_para_string')

			elif valor['classe'] == 'Vendedor' and valor['metodo'] == 'get_quantidade_vendas':
				print(func.get_quantidade_vendas())
			elif valor['classe'] == 'Vendedor' and valor['metodo'] == 'set_quantidade_vendas':
				func.set_quantidade_vendas(valor['novo_quantidade_vendas'])
				print(func._Vendedor__quantidade_vendas)
			elif valor['classe'] == 'Gerente' and valor['metodo'] == 'adicionar_vendedor':
				for item in func._Gerente__vendedores:
					print(item.get_nome(), item.get_cpf(), item.get_dia_nasc(), item.get_mes_nasc(), item.get_ano_nasc(), item.get_salario(), item.get_quantidade_vendas())

			elif valor['classe'] in ['Vendedor', 'Gerente'] and valor['metodo'] == 'calcular_salario_final':
				print('%.2f' % (func.calcular_salario_final()))
			elif valor['classe'] in ['Vendedor', 'Gerente'] and valor['metodo'] == 'converter_para_string':
				print(func.converter_para_string())


def main():
	nome_teste = input()
	valor = eval(input())
	testa_atividade(nome_teste, valor)
main()
