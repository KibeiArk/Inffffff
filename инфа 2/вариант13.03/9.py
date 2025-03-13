f =open('9.txt')
k=0
for s in f:
    a = sorted([int(x) for x in s.split()])
    p4 = [x for x in a if a.count(x)==4]
    p2 = sorted([x for x in a if a.count(x)==2])
    np = [x for x in a if a.count(x)==1]
    if len(p4)==4 and len(p2)==2 and len(np)==3:
        if sum(np)/len(np) >=max(p2[0],p4[0]):
            print(a)
            k+=1
print(k)
