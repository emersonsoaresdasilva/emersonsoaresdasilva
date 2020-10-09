class Filme:

    def __init__(self, titulo, genero):

        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero    


#Programa Principal

lista_filmes = []
i = 1
while i <= 3:
    titulo = input('Informe o título do filme: ')
    genero = input('Informe o genero do filme: ')
    filme = Filme(titulo,genero)
    lista_filmes.append(filme)
    i+=1

print('===============================')
print('     Relatório dos Filmes      ')
print('===============================')
i = 0
while i < len(lista_filmes):
    filme = lista_filmes[i]
    print('Título: ', get_titulo())
    print('Genero: ', get_genero())
    print('-'*20)
    i += 1




