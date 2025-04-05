'''(Е. Джобс) Текстовый файл 24-204.txt содержит строку из 
заглавных латинских букв A, B и C, всего не более чем из 
106 символов. Найдите максимальное количество подряд 
идущих пар символов AA или CC. Искомая подстрока может 
включать только пары АA, только пары CС или 
содержать одновременно как пары АA, так и пары CC.'''
s = open('веб2/7.txt').readline()
c = 0
m=[]
for i in range(0,len(s),2):
    if s[i-1] +s[i] =='AA' or s[i-1] +s[i] =='CC':
        c+=1
    else:
        c=0
    m.append(c)
c=0
for i in range(1,len(s),2):
    if s[i-1] +s[i] =='AA' or s[i-1] +s[i] =='CC':
        c+=1
    else:
        c=0
    m.append(c)
print(max(m))
#1310
s = open('веб2/7.txt').readline()
m = [0] *len(s)
for i in range(1,len(s)):
    if s[i-1]+s[i]=='AA' or s[i-1] + s[i]=='CC':
        m[i] = m[i-2]+1
print(max(m))
#1310