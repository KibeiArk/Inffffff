'''Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три
команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 3
3. Умножить на 4
Сколько существует программ, для которых при исходном числе 2 результатом
является число 60 и при этом траектория вычислений содержит число 16 и не
содержит число 21?'''
def f(x,m):
    if x>m or x ==21:return 0
    if x==m:return 1
    if x<m:return f(x+1,m)+f(x*3,m)+f(x*4,m)
print(f(2,16)*f(16,60))
#40