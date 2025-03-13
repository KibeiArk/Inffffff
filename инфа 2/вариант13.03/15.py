def f(x,y): return (((2*x + 3*y) ==101) and (x+y<a))
for a in range(1,1000):
    if all(f(x,y)==0 for x in range(0,100) for y in range(0,100)):
        print(a)