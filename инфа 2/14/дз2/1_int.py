'''(А. Богданов) Операнды арифметического выражения записаны в системе
счисления с основанием 17:
9759x_17 + 3x108_17
В записи чисел переменной x обозначена неизвестная цифра из алфавита 17-
ричной системы счисления. Определите наименьшее значение x, при котором
значение данного арифметического выражения кратно 11. Для найденного
значения x вычислите частное от деления значения арифметического выражения
на 11 и укажите его в ответе в десятичной системе счисления. Основание
системы счисления в ответе указывать не нужно.
'''
for x in '0123456789abcdefg':
    a = int(f'9759{x}',17) + int(f'3{x}108',17)
    if a%11==0:
        print(x,a//11)
'''
2 95306 <= Ответ
d 100220
'''