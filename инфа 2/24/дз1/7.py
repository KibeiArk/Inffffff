s = open('дз2/24_3021.txt').readline()
s =s.replace('ZXY','*').replace('ZYX','*')
s =s.replace('X',' ').replace('Y',' ').replace('Z',' ')
print(max(len(x) for x in s.split()))
#28