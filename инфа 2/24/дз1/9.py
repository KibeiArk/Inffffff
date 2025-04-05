s=open('дз2/24_6094.txt').readline()
s=s.replace('XYZY','XYZ YZY').replace('XY','*').replace('ZY','*')
s =s.replace('Z',' ').replace('X',' ').replace('Y',' ')
print(max(len(x) for x in s.split()))