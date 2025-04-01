'''(ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита и цифры. 
Определите максимальную длину подстроки, в которой ни одна буква не стоит рядом с буквой и ни одна цифра не стоит рядом с цифрой
'''
s =open('11.txt').readline()
for c in 'QWERTYUIOPSDFGHJKLZXCVBNM':
    s = s.replace(c,'A')
for c in '123456789':
    s = s.replace(c,'0')
while 'AA' in s:
    s =s.replace('AA','A A')
while '00' in s:
    s =s.replace('00','0 0')
print(max(len(x) for x in s.split()))
#18