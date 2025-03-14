'''Назовём маской числа последовательность цифр, в которой также могут
встречаться следующие символы:
– символ «?» означает ровно одну произвольную цифру;
– символ «*» означает любую последовательность цифр произвольной длины; в
том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
Среди натуральных чисел, не превышающих 10^8
 , найдите все числа,
соответствующие маске 12*4?65, делящиеся на 161 без остатка.
В ответе запишите в первом столбце таблицы все найденные числа в порядке
возрастания, а во втором столбце – соответствующие им результаты деления
этих чисел на 161.
'''
from fnmatch import*
for i in range(0,10**8,161):
    if fnmatch(str(i),'12*4?65'):
        print(i,i//161)