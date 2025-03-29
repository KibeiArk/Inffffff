def f(x):return (x%a!=0)<=((x%28==0) <=(x%49!=0))
for a in range(1,100000):
    if all(f(x) for x in range(1,10000)):
        print(a)