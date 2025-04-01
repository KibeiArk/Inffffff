s = open('дз2/24_18186.txt').readline()
s =s.replace('E','A').replace('C','B').replace('D','B').replace('F','B').replace('G','B').replace('H','B')
s =s.replace('BBA','BBA BBA')
print(max(len(x) for x in s.split() if x.count('BBA')==2))
#64