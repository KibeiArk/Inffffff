k=0
for n in range(100,201):
    b= f'{n:b}'
    if len(b)%2==0:
        b+='10'
    else:
        b= '11'+b
    r = int(b,2)
    b= f'{r:b}'
    if len(b)%2==0:
        b+='10'
    else:
        b= '11'+b
    r = int(b,2)
    if r %2==0:
        k+=1
print(k)
#87