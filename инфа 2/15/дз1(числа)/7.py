def f(x,y): return ((x<a) and (y<a) and (x * y>1200))
for a in range(0,100):
    if all(f(x,y)==0 for x in range(0,100) for y in range(0,100)):
        print(a)
#35