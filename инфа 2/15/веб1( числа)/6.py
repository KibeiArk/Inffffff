def  f(x) :return ((x&156!=0)or(x&436!=0)) <=(x&a>0)
for a in range(1,1000):
    if all(f(x) for x in range(0,10000)):
        print(a)
        break