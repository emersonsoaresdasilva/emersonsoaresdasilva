# Definiçao da classe Pessoa
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf

    def exibir(self):
        print('Informações da pessoa física:')
        print('Nome:', self.nome) # atributo herdado da classe Pessoa
        print('Endereço:', self.endereco) # atributo herdado da classe Pessoa
        print('CPF:', self.cpf)

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self.cnpj = cnpj

    def exibir(self):
        print('Informações da pessoa jurídica:')
        print('Nome:', self.nome) # atributo herdado da classe Pessoa
        print('Endereço:', self.endereco) # atributo herdado da classe Pessoa
        print('CNPJ:', self.cnpj)

# Programa principal:
maria = PessoaFisica('Maria Silva', 'Rua da Frente', 12345678900)
loja = PessoaJuridica('Joana Presentes', 'Avenida Principal', 12345678901234)
maria.exibir()
print('='*20)
loja.exibir()


