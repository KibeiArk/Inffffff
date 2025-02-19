def cc(x,s):
    v = ''
    while x >0:
        v = str(x%s) + v
        x = x //s
    return int(v)
for i in range(4,20):
    print(i,cc(381,i))
#18