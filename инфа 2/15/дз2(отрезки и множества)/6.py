def f(x):
    P = 5<=x<=280
    Q = 295<=x<=400
    R = 375<=x<=450
    A = a1<=x<=a2
    return (Q <= P)or((not A) <=R)
d = [y for x in (5,280,295,400,375,450) for y in (x,x+0.01,x-0.01)]
m = []
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(min(m))
#80