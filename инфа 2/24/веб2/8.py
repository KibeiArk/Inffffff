'''Текстовый файл 24-197.txt содержит строку из 
заглавных латинских букв X, Y и Z, всего не более
 чем из 106 символов. Определите максимальное 
 количество идущих подряд троек символов X*X или Y*Y,
 где * обозначает один любой символ.'''
s =open('веб2/8.txt').readline()
m=[]
for j in 2,3,4:
    c = 0
    for i in range(j,len(s),3):
        if s[i-2]+s[i]=='XX' or s[i-2]+s[i]=='YY':
            c +=1
        else:
            c =0
        m.append(c)
print(max(m))
#16
s =open('веб2/8.txt').readline()
m=[0]*len(s)
for i in range(2,len(s)):
    if s[i-2]+s[i]=='XX' or s[i-2]+s[i]=='YY':
        m[i]=m[i-3]+1
print(max(m))
#16