'''Задание № 7() 
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему
новое число R следующим образом.
1) Строится двоичная запись числа N.
2) Далее эта запись обрабатывается по следующему правилу:
a) если количество значащих цифр в двоичной записи числа чётное, то к этой
записи в середину дописывается 1;
б) если количество значащих цифр в двоичной записи числа нечётное, то запись
не изменяется.
Полученная таким образом запись является двоичной записью искомого числа
R. Например, для исходного числа 510= 1012
, результатом является число 1012= 510
 а для исходного числа 210= 102
 результатом является число 1102= 610.
Укажите минимальное число N, после обработки которого с помощью этого
алгоритма получается число R, не меньшее, чем 26. В ответе запишите это
число в десятичной системе счисления. '''
ant=[]
for n in range(1,50):
    b =f'{n:b}'
    if len(b)%2==0:
        b = b[:len(b)//2]+ '1'+ b[len(b)//2:]
    r = int(b,2)
    if r >=26:
        ant.append(n)
print(min(ant))
#12