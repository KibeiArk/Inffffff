''' В файле электронной таблицы в каждой строке записаны 6 натуральных чисел.
Определите количество строк таблицы, содержащих числа, для которых
выполнены следующие условия:
– минимальное число не повторяется;
– среди остальных чисел строки есть повторяющиеся;
– сумма максимального и минимального чисел строки меньше, чем сумма
повторяющихся чисел.'''
f = open('12.txt')
k=0
for s in f:
    a = sorted([int(x) for x in s.split()])
    p = [x for x in a if a.count(x) > 1]
    if a.count(a[0]) ==1 and len(p)>=2:
        if a[0] + a[5] < sum(p):
            k+=1
print(k)
#447
