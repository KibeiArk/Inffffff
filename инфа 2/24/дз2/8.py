s = open('дз2/24_7688.txt').readline()
m = [0]*len(s)
for i in range(1,len(s)):
    if s[i-1] + s[i] =='XA' or s[i-1] + s[i] =='XY':
        m[i]= m[i-2]+2
    if i>=2 and s[i-2] + s[i-1] +s[i] =='TXA':
        m[i]=m[i-3]+3
print(max(m))
#112