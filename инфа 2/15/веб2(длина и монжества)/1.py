def f(x,a1,a2):
    return(a1<=x<=a2) <=((10<=x<=20) or (25<=x<=55))
fa=[]
d=[]
for x in 10,20,25,55:
    d.append(x)
    d.append(x -0.01)
    d.append(x + 0.01)
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x,a1,a2) for x in d):
            fa.append(a2-a1)
print(max(fa))
