'''В файле 17-3.txt содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от -10 000 до 10 000 включительно. Определите и запишите в ответе
сначала количество троек элементов последовательности, в которых произведение кратно 7, а сумма
оканчивается на 5, затем максимальную из сумм элементов таких троек. В данной задаче под
тройкой подразумевается три идущих подряд элемента последовательности.'''
a = [int(x) for x in open('2.txt')]
ans=[]
for x,y,z in zip(a,a[1:],a[2:]):
    if (x*y*z)%7==0 and abs(x+y+z)%10==5:
        ans.append(x+y+z)
print(len(ans),max(ans))
#153 19285
