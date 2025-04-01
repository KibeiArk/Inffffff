s =open('дз2/24_16333.txt').readline()
s = s.replace('2','1').replace('4','1')
s = s.replace('R','Q').replace('W','Q')
while '11' in s: s =s.replace('11','1 1')
while 'QQ' in s: s =s.replace('QQ','Q Q')
print(max(len(x) for x in s.split()))
#17