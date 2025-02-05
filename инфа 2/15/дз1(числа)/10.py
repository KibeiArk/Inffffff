def f(x): return (a%35 ==0) and ((730%x==0) <=((a%x!=0)<=(110%x!=0)))
b=[]
for a in range(1,1001):
    if all(f(x) for x in range(1,1000)):
        b.append(a)
print(len(b))
#14