'''Исполнитель преобразует число на экране. У исполнителя есть три команды,
которые обозначены латинскими буквами:
A. Прибавить 1
B. Умножить на 2
C. Возвести в квадрат
Программа для исполнителя – это последовательность команд.
Сколько существует программ, для которых при исходном числе 2 результатом
является число 20, при этом траектория вычислений не содержит числа 11?'''
def f(x,m):
    if x>m or x==11:return 0
    if x==m:return 1
    if x<m:return f(x+1,m)+ f(x*2,m)+ f (x**2,m)
print(f(2,20))
#37