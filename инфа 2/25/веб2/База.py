'''x = 100000000
a = []
for i in range(1,x+1):
    if x%i ==0:
        a.append(i)
print(a)'''
def div(x):
    d = set()
    #Перебираем числа от 1 до цлеой части корня вкл
    for i in range(1,int(x**0.5)+1):
        if x %i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
print(div(100000000))

