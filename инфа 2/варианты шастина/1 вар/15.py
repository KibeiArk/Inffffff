def f(x,y): return (x<=19)or (y<2*x+a-50)or(y>17)
for a in range(0,100):
    if all(f(x,y) for x in range(0,1000) for y in range(0,1000)):
        print(a)