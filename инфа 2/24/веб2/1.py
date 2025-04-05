'''
(А.М. Кабанов) В текстовом файле k7a-2.txt находится 
цепочка из символов латинского алфавита A, B, C, D, E, F. 
Найдите длину самой длинной подцепочки, состоящей из 
символов A, C, D (в произвольном порядке).'''
'''s = open('веб2/1.txt').readline()
c =0
m =[]
for i in range(len(s)):
    if s[i] in 'ACD':
        c+=1
    else:
        c =0
    m.append(c)
print(max(m))
#11'''

s = open('веб2/1.txt').readline()
m = [0]*len(s)
for i in range(len(s)):
    if s[i] in 'ACD':
        m[i]=m[i-1] +1
print(max(m))
#11