'''В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от 0 до 10 000 включительно. Определите количество пар, в которых
хотя бы один из двух элементов больше, чем среднее арифметическое всех чисел в файле, а их
сумма делится на 7. В ответе запишите два числа: сначала количество найденных пар, а затем –
минимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих
подряд элемента последовательности.'''
a = [int(x) for x in open('4.txt')]
ar = sum(a)//len(a)
ans=[]
for x,y in zip(a,a[1:]):
    if (x >ar or y>ar) and (x+y)%7==0:
        ans.append(x+y)
print(len(ans),min(ans))
#202 6916
