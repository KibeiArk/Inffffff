def f(x,m):
    if x>=54:return m%2==0
    if m==0: return 0
    h = [f(x+2,m-1),f(x*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print(19,[s for s in range(1,54) if f(s,2) and not f(s,1)])
#25
print(20,[s for s in range(1,54) if f(s,3)and not f(s,1)])
print(21,[s for s in range(1,54) if f(s,4) and not f(s,2)])
'''
19 [25, 26]
20 [13, 23, 24]
21 [21, 22]
'''