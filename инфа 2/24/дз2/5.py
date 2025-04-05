s =open('дз2/24_3760.txt').readline()
m=[0]*len(s)
for i in range(2,len(s)):
    if s[i-2]+s[i]=='XY' or s[i-2]+s[i]=='ZY':
        m[i] = m[i-3]+3
print(max(m)//3)
#20