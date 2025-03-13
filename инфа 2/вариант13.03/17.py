f = [int(x) for x in open('17_11838.txt')]
n = max([x for x in f if abs(x)%100==50])
ans=[]
for x,y,z in zip(f,f[1:],f[2:]):
    if x != y !=z:
        if (10000<=abs(x))+(10000<=abs(y))+(10000<=abs(z))==3:
            if x + z +y <=n:
                print(x,z,y)
                ans.append(x+z+y)
print(len(ans),max(ans))