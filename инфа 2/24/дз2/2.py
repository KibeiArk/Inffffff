s = open('дз2/24_2478.txt').readline()
m=[2]*len(s)
for i in range(2,len(s)):
    if  not s[i-2]==s[i-1]==s[i]:
        m[i] = m[i-1]+1
print(max(m))
#1080