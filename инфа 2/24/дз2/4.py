s =open('дз2/24_1302.txt').readline()
s = s.replace('XZZY','XZZ ZZY')
print(max(len(x) for x in s.split()))
#1713