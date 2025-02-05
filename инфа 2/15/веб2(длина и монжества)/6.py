# Наименьшее
a = set()
def f(x):
    P = x in {2,4,9,10,15}
    Q = x in {3,8,9,10,20}
    A = x in a
    return(not(P==A)) <= (Q==A)
for x in range(1,100):
    if f(x)==0:
        a.add(x)
print(a)
#90