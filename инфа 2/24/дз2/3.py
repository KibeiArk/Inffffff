s = open('дз2/24_7853.txt').readline()
m =[2]*len(s)
for i in range(2,len(s)):
    if not(s[i] in 'NOT' and s[i-2] in 'NOT'):
        m[i] = m[i-1] +1
print(max(m))#1461