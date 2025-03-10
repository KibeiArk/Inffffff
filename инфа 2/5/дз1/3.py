'''На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему
новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются ещё два разряда по следующему правилу:
а) если N чётное, то к нему справа приписываются две последние цифры его
двоичной записи;
б) если N нечётное, то к нему справа и слева приписывается цифра 1.
Полученная таким образом запись (в ней на два разряда больше, чем в записи
исходного числа N) является двоичной записью искомого числа R.
Например, двоичная запись нечётного числа 110012
 будет преобразована в
11100112
.
Укажите такое наименьшее число R, превышающее 130, которое может являться
результатом работы данного алгоритма.
В ответе это число запишите в десятичной системе счисления'''
ant = []
for n in range(1,1000):
    b = f'{n:b}'
    if n%2==0:
        b= b + b[-2] +b[-1]
    else:
        b = '1'+b+'1'
    r = int(b,2)
    if r>130:
        ant.append(r)
print(min(ant))
#138