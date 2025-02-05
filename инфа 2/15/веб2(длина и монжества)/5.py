# Множество Наименьшее
a = set()
def f(x):
    P = x in {1,2,3,4}
    Q = x in {1,2,3,4,5,6}
    A = x in a
    return (not A)<=((not P) or(not Q))
for x in range(1,100):
    if f(x)==0:
        a.add(x)
print(len(a))
#4