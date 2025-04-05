s = open('дз2/24_5223.txt').readline()
s =s.replace('DD','D D').replace('DD','D D')
print(max(len(x) for x in s.split() if 'FE' in x))
#2486