def f(x):
    P = 15<=x<=40
    Q =21<=x<=63
    A = a1<=x<=a2
    return P <=((Q and (not A)) <= (not P))
d = [y for x in (15,40,21,63) for y in (x,x+0.01,x-0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(min(m))
#19