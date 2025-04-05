s = open('дз2/24_4555.txt').readline()
m = [0]*len(s)
for i in range(1,len(s)):
    if s[i-1] + s[i]=='XY':
        m[i]=m[i-2]+2
    if i>=2 and s[i-2] + s[i-1]+s[i]=='ZZX':
        m[i] =m[i-3]+3
print(max(m))
#22