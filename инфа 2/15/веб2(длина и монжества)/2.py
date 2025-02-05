def f(x,a1,a2):
    P = 1023<=x<=2148
    Q = 1362<=x<=3898
    R = 1813<=x<=2566
    A = a1<=x<=a2
    return (not(Q <= (P or R))) <= ((not A) <= (not Q))
d = []
m=[]
for x in 1023,2148,1362,3898,1813,2566:
    d.append(x)
    d.append(x - 0.00000000001)
    d.append(x + 0.00000000001)
for a1 in d:
    for a2 in d:
        if a2 >=a1  and all(f(x,a1,a2) for x in d):
            m.append(a2-a1)
print(min(m))
#1332