def f(x,m):
    if x > m or x ==22: return 0
    if x ==m:return 1
    if x<m : return f(x+3,m)+f(x+4,m)
print(f(16,38))
#16