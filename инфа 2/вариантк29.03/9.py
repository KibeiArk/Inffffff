f = open('9.txt')
k=0
for s in f:
    a = sorted([int(x) for x in s.split()])
    np = sorted([x for x in a if a.count(x)==1])
    if len(np)==5:
        if a[2]*2 > a[-1] and a[2]*2 >a[0]*3:
            k+=1
            print(a)
print(k)