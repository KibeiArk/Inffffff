'''def f(s,x):
    d = ''
    while x >0:
        d = str(x%s) + d
        x = x//s
    return int(d)
for x in range(1,11):
    print(x,f(x,50))'''
def tri(x):
    s = ''
    while x > 0:
        s = str(x%8)+s
        x = x//8
    return s
print(tri(50))