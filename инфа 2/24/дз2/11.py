s = open('дз2/24_8959.txt').readline()
s = s.replace('NPC','***').replace('EA','**')
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s =s.replace(i,' ')
print(max(len(x) for x in s.split()))