'''Значение арифметического выражения
7 *512**1912 + 6 * 64**1954 - 5 * 8**1991 -4 * 8**1980 - 2022

записали в системе счисления с основанием 8. Определите количество цифр 7 в
записи этого числа.
'''
a = 7 *512**1912 + 6 * 64**1954 - 5 * 8**1991 -4 * 8**1980 - 2022
k=0
while a >0:
    if a%8==7:
        k+=1
    a = a//8
print(k)
#3903