'''Задача №2 (3560)
 (Е.А. Мирончик) Сколько цифр в восьмеричной записи числа
2**299+2**298+2**297+2**296?
'''
x = 2**299+2**298+2**297+2**296
a =f'{x:o}'
print(len(a))
#100