f = [int(x) for x in open('17_2017.txt')]
ans=[]
for x in f:
    a = str(hex(x))
    if a[-1]=='b' and x%7==0 and x%6!=0 and x %19!=0 and x %13!=0:
        ans.append(x)
print(sum(ans),len(ans))
#74452 12