def f(x):
    P = 20<=x<=85
    Q = 30<=x<=65
    A = a1<=x<=a2
    return(P==Q)<=(not A)
d = [y for x in range(1,100) for y in (x,x+0.01,x-0.01)]
k=0
for a1 in range(1,100):
    for a2 in range(1,100):
        if a2>a1 and all(f(x) for x in d)  :
            k+=1
print(k)
#235