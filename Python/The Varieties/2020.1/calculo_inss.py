SB = float(input())

if SB <= 1751.81:
    contribuicao = SB * 0.08
elif SB <= 2919.72:
    contribuicao = SB * 0.09
elif SB <= 5839.45:
    contribuicao = SB * 0.11
else:
    contribuicao = 5839.45 * 0.11

print('Desconto do INSS: R$ %.2F' % contribuicao)
