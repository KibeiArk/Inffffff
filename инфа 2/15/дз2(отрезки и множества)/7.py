a = set()
def f(x):
    P = x in {1,3,4,9,11,13,15,17,19,21}
    Q = x in {3,6,9,12,15,18,21,24,27,30}
    A = x in a
    return (P <= A) or ((not A) <= (not Q))
for x in range(1,100):
    if f(x)==0:
        a.add(x)
s =1
for i in a:
    s *=i
print(s)