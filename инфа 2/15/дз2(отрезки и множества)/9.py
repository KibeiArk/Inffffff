from itertools import*
def f(x):
    P = x[0]+x[1]=='01'
    Q = x[-1]=='1'
    A = x in s
    return  Q <= (P or A)
s=set()
for x in product('01',repeat=16):
    a = ''.join(x)
    if f(a)==0:
        s.add(a)
print(len(s))
#24576