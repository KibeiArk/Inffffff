'''Значение арифметического выражения 7**2+49**4-21 записали в
системе счисления с основанием 14. В этой записи помимо цифр от 0 до 9
могут встречаться цифры из списка: А, B, С, D, которые имеют числовые
значения от 10 до 13 соответственно. Сколько цифр A и цифр 0 встречается в
этой записи?'''
a = 7**2+49**4-21
k=0
while a >0:
    if a%14 == 10 or a %14 ==0:
        k+=1
    a =a//14
print(k)
#3