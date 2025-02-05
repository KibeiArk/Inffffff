def f(x):
    P = 15<=x<=40
    Q = 35<=x<=60
    A = a1<=x<=a2
    return((not Q) or P)and A
d = [y for x in (15,40,35,60) for y in (x,x+0.01,x-0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x)==0 for x in d):
            m.append(a2-a1)
print(max(m))
#20