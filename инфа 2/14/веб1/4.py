'''(В. Шелудько) Значение выражения 4**1103+3*4**1444-2*4**144+66 записали в системе
счисления с основанием 4. Найдите сумму цифр получившегося числа и
запишите её в ответе в десятичной системе счисления
'''
a = 4**1103+3*4**1444-2*4**144+66
s = []
while a > 0:
    s.append(a%4)
    a = a//4
print(sum(s))
#2882