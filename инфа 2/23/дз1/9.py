'''Исполнитель преобразует число на экране. У исполнителя есть две команды,
которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
Сколько существует программ, которые преобразуют исходное число 1 в число
60 так, что в процессе выполнения на экране ни разу не появляется цифра 5?'''
def f(x,m):
    if x>m or '5' in str(x):return 0
    if x==m:return 1 
    if x<m:return f(x+1,m)+f(x*2,m)
print(f(1,60))
#18