def f(x,m):
    if x>m:return 0
    if x==m:return 1
    if x<m:return f(x+1,m) +f(x*2,m)
print(f(4,8)*f(8,10)*f(10,15))