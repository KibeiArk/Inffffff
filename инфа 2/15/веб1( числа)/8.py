def f(x,y):return (3*y + 2*x <a) or (x>8) or (y>12)
for a in range(1,100):
    if all(f(x,y) for x in range(1,100) for y in range(1,100)):
        print(a)
        break