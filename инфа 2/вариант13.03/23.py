def f(x,m):
    if x>m or x == 26: return 0
    if x == m:return 1
    if x<m: return f(x+1,m) + f(x*2,m)
print(f(2,11)*f(11,39))