'''В какой системе счисления выполняется равенство ? В
21_X * 13_X = 313_X
ответе укажите число – основание системы счисления.
'''
for x in range(4,36):
    if int('21',x) * int('13',x) == int('313',x):
        print(x)
#6