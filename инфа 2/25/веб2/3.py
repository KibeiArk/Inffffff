'''Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому
 числу. Найдите все натуральные числа, принадлежащие отрезку [152346; 957812] и имеющие ровно
 три нетривиальных делителя. Для каждого найденного числа запишите в ответе само число и его
 наибольший нетривиальный делитель. Найденные числа расположите в порядке возрастания.'''
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
'''for x in range(152346,957813):
    d =div(x)
    if len(d)==3:
        print(x,d)'''
for i in range(391,978+1):
    x = i**2
    d =div(x)
    if len(d)==3:
        print(x,d[-1])
'''
279841 12167
707281 24389
923521 29791
'''