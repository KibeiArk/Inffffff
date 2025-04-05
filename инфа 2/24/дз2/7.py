s = open('дз2/24_16269.txt').readline()
while 'XXXX' in s:s=s.replace('XXXX','XXX XXX')
while 'YYYY' in s:s=s.replace('YYYY','YYY YYY')
while 'ZZZZ' in s:s=s.replace('ZZZZ','ZZZ ZZZ')
m=[0]*len(s)
for i in range(1,len(s)):
    if s[i-1]+s[i] =='XX' or s[i-1]+s[i] =='YY'or s[i-1]+s[i] =='ZZ':
        m[i]=m[i-2]+2
print(max(m)) 
#52