'''(Е. Джобс) Текстовый файл 24-j5.txt состоит не более чем из 106 символов 
S, T, O, C, K. Определите максимальное количество подряд идущих комбинаций «KOT».
Показать ответ
'''
f = open('2.txt').readline()
for i in range(1,10):
    print(i,i*'KOT' in f)
#2
'''
1 True
2 True
3 False
4 False
5 False
6 False
7 False
8 False
9 False
'''