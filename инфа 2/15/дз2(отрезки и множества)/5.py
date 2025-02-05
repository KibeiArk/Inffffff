def f(x):
    B = 24<=x<=90
    C = 47<=x<=115
    A = a1<=x<=a2
    return C <=(((not A)and B) <= (not C))
d = [y for x in (24,90,47,115) for y in (x,x+0.01,x-0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(min(m))
#43
