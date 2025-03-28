'''В файле содержится последовательность натуральных чисел, каждое из которых
не превышает 100 000. Определите количество троек
элементов последовательности, в которых ровно два из трёх элементов
являются трёхзначными числами, а сумма элементов тройки не
больше максимального элемента последовательности, оканчивающегося на 13.
Гарантируется, что в последовательности есть хотя бы одно
число, оканчивающееся на 13. В ответе запишите количество найденных
троек чисел, затем максимальную из сумм элементов таких троек. В данной
задаче под тройкой подразумевается три идущих подряд
элемента последовательности.
'''
a = [int(x) for x in open('дз1//17_10100.txt')]
ans =[]
n=max([i for i in a if i%100==13])
for x,y,z in zip(a,a[1:],a[2:]):
    if (100<=x<1000)+(100<=y<1000)+(100<=z<1000)==2 and (x+y+z) <=n:
        ans.append(x+y+z)
print(len(ans),max(ans))
#959 97471