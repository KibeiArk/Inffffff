def f(x,s,m):
    if x+s>=200: return m%2==0
    if m==0:return 0
    h = [f(x+6,s,m-1),f(x**2,s,m-1),f(x,s+6,m-1),f(x,s**2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in (1,195) if not f(3,s,1) and f(3,s,2)])
print([s for s in (1,195) if not f(3,s,1) and f(3,s,3)])
print([s for s in (1,195) if not f(3,s,2) and not f(3,s,4) and f(3,s,6)])
