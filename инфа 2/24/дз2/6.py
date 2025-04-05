s = open('дз2/24_5139.txt').readline()
for c in 'BCDF': s =s.replace(c,"B")
for c in 'AEU': s = s.replace(c,'A')
m=[0]*len(s)
for i in range(2,len(s)):
    if s[i-2]+s[i-1]+s[i]=='BAB':
        m[i] = m[i-3]+3
print(max(m)//3)
#6