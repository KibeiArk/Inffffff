def f(x):
    B = 25<=x <=40
    C = 12<=x<=33
    A = a1<=x<=a2
    return(B <=A)and((not C) or A)
d = [y for x in (25,40,12,33) for y in (x,x+0.01,x-0.01)]
m=[]
for a1 in d:
    for a2 in d:
        if a2 >=a1 and all(f(x) for x in d):
            m.append(a2-a1)
print(min(m))
#28