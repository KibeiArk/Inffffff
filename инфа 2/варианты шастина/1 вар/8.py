from itertools import*

k=0
for i in product('БЕНРСТЬЯ',repeat = 5):
    k+=1
    a = ''.join(i)
    if k%2==0 and a[0]=='Р' and a.count('Ь')==0:
        print(k,a)
#16384