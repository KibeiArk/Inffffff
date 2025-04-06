a = [int(x) for x in open('17_17750.txt')]
b = min(a)
ans=[]
for i in range(0,len(a)-1):
    if (a[i]%77)+(a[i+1]%77)==b:
        ans.append(a[i]+a[i+1])
print(len(ans),max(ans))