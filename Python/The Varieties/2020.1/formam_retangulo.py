def formam_retangulo(A,B,C,D):
    if C == B or D == A or B == A or C == D:
        print('formam um retangulo')
    else:
        print('nao formam um retangulo')

A = int(input())
B = int(input())
C = int(input())
D = int(input())

formam_retangulo(A,B,C,D)
