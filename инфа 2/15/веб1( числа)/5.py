def f(x):return ( x%12==0) and  (70<=x <=80) and (x%a!=0)
k=0
for a in range(1,10000):
    if all(f(x)==0 for x in range(1,100000)):
        k+=1
print(k)