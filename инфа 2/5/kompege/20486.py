'''(М. Попков) На вход алгоритма подаётся натуральное число N>3. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются ещё три разряда по следующему правилу:
а) если N чётное, то к нему справа приписываются три его первые цифры двоичной записи;
б) если N нечётное, то к нему слева приписывается 1, а справа приписывается 01.
Полученная таким образом запись (в ней на три разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R. Укажите минимальное число R, которое превышает число 600 и может являться результатом работы данного алгоритма.
В ответе это число запишите в десятичной системе счисления.'''
ans=[]
for n in range(10,100):
    b = f'{n:b}'
    if n%2==0:
        b += b[:3]
    else:
        b = '1'+b+'0'
    r = int(b,2)
    if r>600:
        ans.append(r)
print(min(ans))
#612