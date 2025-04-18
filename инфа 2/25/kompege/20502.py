'''№ 20502 (Уровень: Средний)
(В. Зарянкин) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
1) символ «@» означает ровно одну произвольную нечётную цифру;
2) символ «#» означает любую последовательность чётных цифр произвольной длины; в том числе «#» может задавать и пустую последовательность.
Например, маске 123#4@5 могут соответствовать числа 123405 и 12300405.
Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 20@@22#, делящиеся на 10980 без остатка.
В ответе запишите в первом столбце таблицы первые 5 найденных чисел в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 10980.
Количество строк в таблице для ответа избыточно.'''
from itertools import *
answers=[]
for c in range(6):
    for d1 in '13579':
        for d0 in '13579':
            for r in product('02468',repeat=c):
                s='20'+d1+d0+'22'+''.join(r)
                if int(s)%10980==0 and int(s)<=10**10:
                    answers.append((int(s), int(s)//10980))

answers =sorted(answers)
for i in range(5):
    print(answers[i][0],answers[i][1])
'''
2075220 189
20192220 1839
20752200 1890
201922200 18390
207522000 18900
'''