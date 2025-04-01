s = open('дз2/24_2942.txt').readline()
s =s.replace('AB','*').replace('AC','*')
s =s.replace('B',' ').replace('C',' ').replace('A',' ')
print(max(len(x) for x in s.split()))
#2397