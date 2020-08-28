Media,Aulas,Faltas = input().split()

Media = float(Media)
Aulas = int(Aulas)
Faltas = int(Faltas)

Frequencia = (((Aulas - Faltas)/ Aulas) * 100)

if(Frequencia >= 75 and Media >= 5) or (Frequencia >= 50 and Media >= 7):
    print('APROVADO')
else:
    print('REPROVADO')
