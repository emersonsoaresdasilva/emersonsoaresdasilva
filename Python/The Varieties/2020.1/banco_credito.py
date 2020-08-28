SM = float(input())

if (SM > 4000.00):
    print('R$ %.2F' % (SM * 0.30))
elif (3000.01 <= SM and SM <= 4000.00):
    print('R$ %.2F' % (SM * 0.25))
elif (2000.01 <= SM and SM <= 3000.00):
    print('R$ %.2F' % (SM * 0.20))
else:
    print('R$ %.2F' % (SM * 0.10))

'''
SM = float(input())

if (SM > 4000.00):
    print('R$ %.2F' % (SM * 0.30))
elif (SM >= 3000.01):
    print('R$ %.2F' % (SM * 0.25))
elif (SM >= 2000.01):
    print('R$ %.2F' % (SM * 0.20))
else:
    print('R$ %.2F' % (SM * 0.10))
'''
