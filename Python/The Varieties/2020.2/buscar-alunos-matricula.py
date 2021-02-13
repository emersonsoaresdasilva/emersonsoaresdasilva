# Implemente a funcao buscar(alunos, matricula) com o que foi pedido no enunciado.
# Lembrete: o parametro alunos eh um dicionario, e o parametro matricula um numero inteiro.

def buscar(alunos, matricula):
    try:
        if (type(matricula) is not int):
            raise TypeError

        elif (len(str(matricula)) != 6):
            raise ValueError
        
        return alunos[matricula]

    except TypeError:
        print('O parametro matricula deve ser inteiro!')
    except ValueError:
        print('O numero de matricula deve ter 6 digitos!')
    except KeyError:
        print('Nao existe aluno com este numero de matricula!')
        
# Programa principal (ja implementado, voce nao precisa se preocupar a partir deste ponto):
dicionario_alunos = {123456: 'Joao', 202018: 'Maria', 202088:'Jose', 202015: 'Bia', 202010: 'Caio'}
num_matricula = input()
try:
	num_matricula = int(num_matricula)
except:
	pass
nome_aluno = buscar(dicionario_alunos, num_matricula)
if nome_aluno is not None:
	print(nome_aluno)
