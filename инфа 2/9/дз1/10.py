''' Откройте файл электронной таблицы, содержащей в каждой строке семь
натуральных чисел. Определите сумму всех чисел в строке таблицы с
наименьшим номером,
для чисел которой выполнены оба условия:
--в строке есть два числа, каждое из которых повторяется дважды, остальные
три числа различны;
— максимальное число строки не повторяется.'''
f = open('10.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    p2 = [x for x in a if a.count(x)==2]
    np = [x for x in a if a.count(x)==1]
    if len(p2)==4 and len(np)==3 and a.count(a[6]) ==1:
        print(sum(a))
        break
#261
