from itertools import*
k=0
for i in product('ABCX',repeat=5):
    a = ''.join(i)
    if (a[-1]=='X' and a.count('X')==1) or a.count('X')==0:
        print(a)
        k+=1
print(k)