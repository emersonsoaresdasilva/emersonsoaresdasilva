#Manipulação de dicionários de dados e tuplas.

'''
O dicionário de dados, que, assim como as listas devem ser utilizados com dados voláteis em memória.
'''

#Estrutura de um dicionário de dados.
usuarios = {}
usuarios = {
    "Chaves":["Chaves Silva", "17/06/2017", "Recep_01"],
    "Quico":["Enrico Flores", "03/06/2017", "Raiox_02"]
}

usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]

#Se, por um engano, você colocar dois objetos com a mesma chave, o segundo objeto irá sobrescrever o primeiro.
usuarios = {}
usuarios = {
    "Chaves":["Chaves Silva", "17/06/1975", "Recep_01"],
    "Quico":["Enrico Flores", "03/06/1976", "Raiox_02"],
    "Quico":["Enrico Flores", "03/06/1976", "Raiox_03"]
}
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]

#Veremos agora como podemos retornar os dados de um objeto da lista.
print(usuarios)
print("="*50)
print("Dados:", usuarios.get("Chaves"))

'''
[...] não precisamos criar um foreach para localizar uma informação dentro do dicionário [...]

O método get(), que recebe um dado pesquisa entre as chaves que existem dentro do dicionário,
caso ele encontre, retornará os dados relativos à chave encontrada.
'''
