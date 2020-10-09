class Pessoa:

    def __init__(self, id, nome):

        self.id = id
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id
 
class PessoaFisica(Pessoa): #Herdando da classe pessoa.

    def __init__(self, id, nome, rg, cpf):
        super().__init__(id, nome)
        self.rg = rg
        self.cpf = cpf
        
class PessoaJuridica(Pessoa):

    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj

pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111" )
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")
print(pessoa1.id)       # 1
print(pessoa1.nome)     # Nome da Pessoa
print(p_juridica.id)    # 2
print(p_juridica.nome)  # Nome da Pessoa Juridica
print(p_juridica.cnpj)  # 1111111111
print(p_fisica.id)      # 3
print(p_fisica.nome)    # Nome da Pessoa Fisica
print(p_fisica.rg)      # 222222222
print(p_fisica.cpf)     # 333333333
