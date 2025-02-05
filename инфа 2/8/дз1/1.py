'''Иван составляет 6-буквенные слова из букв A, B, C, W, X, Y, Z. Первой и
последней буквами этого слова могут быть только буквы W, X, Y, и Z, на
остальных позициях эти буквы не встречаются. Сколько различных кодовых слов
может составить Иван?'''
from itertools import*
k=0
for i in product('ABCWXYZ',repeat=6):
    a = ''.join(i)
    a =a.replace('X','W').replace('Y','W').replace('Z','W')
    if a.count('W')==2:
        if a[0] in 'W' and a[-1] in 'W':
            k+=1
print(k)
#1296