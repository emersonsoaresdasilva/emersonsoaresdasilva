class Livro:
    def __init__(self, titulo, autor, num_paginas): #Criando atributos da classe.

        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

#Programa Principal

livro1 = Livro('Ágape', 'Pe Marcelo Rossi', 150)
livro2 = Livro('Introduction Python', 'C. Dierbach', 357)
        
print('Nome do livro:', livro1.titulo)
print('Autor do livro:', livro1.autor)
print('Número de páginas:', livro1.num_paginas)

print('--' * 15)

print('Nome do livro:', livro2.titulo)
print('Autor do livro:', livro2.autor)
print('Número de páginas:', livro2.num_paginas)
