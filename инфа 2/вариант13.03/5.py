ans=[]
for i in range(1,10000):
    a = f'{i:b}'
    if a.count('1')%2==0:
        a +='1'
    else:
        a +='0'
    if int(a,2)%2==0:
        a +='10'
    else:
        a +='01'
    r = int(a,2)
    if r<1000:
        ans.append(r)
print(max(ans))