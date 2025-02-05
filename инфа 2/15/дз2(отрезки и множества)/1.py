def f(x):
    P = 23<= x < 45
    Q = 34<=x <=56
    A = a1<=x<=a2
    return (not A) or (not P) and Q
d = [y for x in (23,45,34,56) for y in(x, x+0.01,x -0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2>= a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(max(m))
#11