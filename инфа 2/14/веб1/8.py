'''(К. Багдасарян) Значение арифметического выражения 6**900+6**10-x, где х –
натуральное число, не превышающее 10000, записали в системе счисления с
основанием 6. Определите максимальное значение x, при котором данная запись
содержит одинаковое количество цифр «3» и «5».
'''
ant=[]
for a in range(1,10000):
    x = 6**900+6**10-a
    k3=0
    k5=0
    while x > 0:
        if x %6==3:
            k3+=1
        if x %6==5:
            k5+=1
        x = x//6
    if k3 == k5:
        ant.append(a)
print(max(ant))
#9591