a = 5**2 *7**25+6**2*7**36 -4**2 *9**3
k=0
s=''
while a>0:
    s = str(a%7)+s
    if a%7==0:
        k+=1
    a = a//7
print(k,s)
#10