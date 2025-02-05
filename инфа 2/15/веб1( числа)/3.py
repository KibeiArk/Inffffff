def f(x): return (x%33==0) <= ((x%a!=0) <=(x%242!=0))
for a in range(1,10000):
    if all(f(x) for x in range(1,100000)):
        print(a)
#726  