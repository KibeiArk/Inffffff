'''НАЧАЛО
    ПОКА нашлось (12) ИЛИ нашлось (322) ИЛИ нашлось (222)
       ЕСЛИ нашлось (12)
           ТО заменить (12, 2)
       КОНЕЦ ЕСЛИ
       ЕСЛИ нашлось (322)
           ТО заменить (322, 21)
       КОНЕЦ ЕСЛИ
       ЕСЛИ нашлось (222)
           ТО заменить (222, 3)
       КОНЕЦ ЕСЛИ
    КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся с цифры «1», а затем содержащая n цифр «2» (3 < n < 10 000).
Определите наименьшее значение n, при котором сумма цифр в строке, получившейся в результате выполнения программы, равна 15.'''

for n in range(4,10000):
    s = '1' + '2'*n
    su = 0
    while '12' in s or '322' in s or '222' in s :
        if '12' in s:
            s = s.replace('12','2',1)
        if '322' in s:
            s = s.replace('322','21',1)
        if '222' in s:
            s = s.replace('222','3',1)
    if sum(int(x) for x in s) ==15:
        print(n)
        break
#37