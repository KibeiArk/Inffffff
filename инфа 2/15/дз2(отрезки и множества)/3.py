def f(x):
    P = 10<=x<=25
    Q =15<=x<=30
    R = 25<=x<=40
    A =a1<=x<=a2
    return (Q <=(not R)) and A and (not P)
d = [y for x in (10,25,15,30,40) for y in (x,x+0.01,x-0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x)==0 for x in d):
            m.append(a2-a1)
print(max(m))
#20