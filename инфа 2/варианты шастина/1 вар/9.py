f = [x for x in open('9.txt')]
k=0
for s in f:
    a = sorted([int(x) for x in s.split()])
    p5 = [x for x in a if x %10==5]
    if (a[3]+a[4])*2 > (a[0]+a[1]+a[2])*3 and len(p5)>=2:
        k+=1
        print(a)
print(k)
#35