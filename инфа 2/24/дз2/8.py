s = open('дз2/24_4643.txt').readline()
s =s.replace('B','A').replace('2','1')
s = s.replace('11A','*').replace('1',' ').replace('A',' ')
print(max(len(x) for x in s.split()))