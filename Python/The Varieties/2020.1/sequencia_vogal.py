'''
letra = input('Letra: ')

if letra in 'aeiouAEIOU':print('É vogal!')
else:print('Consoante')
'''
#Segunda versão!
letra = input('Letra: ')
print('É vogal' if letra in 'aeiouAEIOU' else 'Consoante')
