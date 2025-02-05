def f(x):
    P = 55<=x<=80
    Q = 20<=x<=105
    A = a1<=x<=a2
    return Q<=((P==Q) or ((not P)<=A))
d =[y for x in (55,80,20,105) for y in (x,x+0.01,x -0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(min(m))
#85