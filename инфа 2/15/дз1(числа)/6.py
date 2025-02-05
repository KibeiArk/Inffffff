def f(x): return(x&30!=4) or((x&35==1)<=(x&a==0))
for a in range(1,1000):
    if all(f(x) for x in range(1,100000)):
        print(a)
#58