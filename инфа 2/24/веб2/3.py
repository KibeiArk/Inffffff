'''(Демовариант 2021 г.) Текстовый файл 24.txt состоит 
не более чем из 106 символов X, Y и Z. Определите 
максимальное количество идущих подряд символов, 
среди которых каждые два соседних различны.'''
'''s = open('веб2/3.txt').readline()
c = 1
m=[]
for i in range(1,len(s)):
    if s[i-1] !=s[i]:
        c+=1
    else:
        c =1
    m.append(c)
print(max(m))
#35'''
s = open('веб2/3.txt').readline()
m=[1]*len(s)
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        m[i] = m[i-1] +1
print(max(m))
#35