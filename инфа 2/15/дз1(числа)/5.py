def f(x): return( (x & 103 == 0) and (x & 94 != 0)) <=(x & a!= 0)
for a in range(1,1000000):
    if all(f(x)==1 for x in range(0,100000)):
        print(a)
        break
#24