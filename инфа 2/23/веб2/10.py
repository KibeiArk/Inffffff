'''У исполнителя Калькулятор имеются три команды, которые обозначены латинскими буквами:
A. Прибавить 1
B. Прибавить 4
C. Умножить на 2
Программа для исполнителя – это последовательность команд, каждая из которых изменяет число.
Требуется найти количество таких программ, которые преобразуют исходное число 1 в число 50, и
при этом траектория вычислений содержит ровно одно из чисел 8, 16, или 32.
'''
def f(x,m):
    if x > m or x==16 or x ==32:return 0
    if x==m:return 1
    if x<m:return f(x+1,m)+f(x+4,m)+f(x*2,m)
a=f(1,8)*f(8,50)
def f(x,m):
    if x > m or x==8 or x ==32:return 0
    if x==m:return 1
    if x<m:return f(x+1,m)+f(x+4,m)+f(x*2,m)
b =f(1,16)*f(16,50)
def f(x,m):
    if x > m or x==16 or x ==8:return 0
    if x==m:return 1
    if x<m:return f(x+1,m)+f(x+4,m)+f(x*2,m)
c=f(1,32)*f(32,50)
print(a+c+b)
#6370599