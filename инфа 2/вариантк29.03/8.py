from itertools import*
k=0
for i in product('ВЬЮГА',repeat=6):
    a = ''.join(i)
    if 'ЮГ' in a:
        print(a)
        k+=1
print(k)