# Definiçao da classe Pessoa
class Pessoa:

    def __init__(self, nome, endereco):

        self.nome = nome
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco
    
# Definição da classe PessoaFisica
class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, cpf):

        super().__init__(nome, endereco)
        self.cpf = cpf

# Definição da classe PessoaJuridica
class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco, cnpj):

        super().__init__(nome, endereco)
        self.cnpj = cnpj
        
'''
joao = PessoaFisica('João da Silva', 'Rua ABC', 12345678900)
print('Nome:', joao.get_nome())
print('Endereço:', joao.get_endereco())
'''

# Programa principal:
maria = PessoaFisica('Maria Silva', 'Rua da Frente', 12345678900)
loja = PessoaJuridica('Joana Presentes', 'Avenida Principal', 12345678901234)
print('Maria é do tipo PessoaFisica?', isinstance(maria, PessoaFisica))
print('Maria é do tipo Pessoa?', isinstance(maria, Pessoa))
print('Maria é do tipo PessoaJuridica?', isinstance(maria, PessoaJuridica))
print('Nome da pessoa física:', maria.get_nome()) # m ́etodo herdado da classe Pessoa
print('Endereço da pessoa física:', maria.get_endereco()) # m ́etodo herdado da classe Pessoa
print('Nome da pessoa jurídica:', loja.get_nome()) # m ́etodo herdado da classe Pessoa
print('Endereço da pessoa jurídica:', loja.get_endereco()) # m ́etodo herdado da classe Pessoa
