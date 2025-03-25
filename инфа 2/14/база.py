def cc10(a,n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s += a[i]*n**i
    return s