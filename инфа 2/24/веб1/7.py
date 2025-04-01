'''Текстовый файл 24-196.txt содержит строку из заглавных латинских букв X, Y и Z, всего не более чем из 106 символов. 
Определите максимальное количество идущих подряд пар символов ZX или ZY.'''
s = open('7.txt').readline()
s = s.replace('ZX','*').replace('ZY','*')
s = s.replace('X',' ').replace('Y',' ').replace('Z',' ')
print(max(len(x) for x in s.split()))
#177