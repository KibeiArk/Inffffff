'''УГОЛ(37, A, x + 45) ≡ УГОЛ(A, x, 90) ∧ ¬(A + 23 < 120)'''
def trey(x,y,a): return x + y +a ==180
def f(x,a):
    return trey(37,a,x+45) == (trey(a,x,90) and not(a+23<120))
for a in range(1,100):
    if all(f(x,a) for x in range(1,10000)):
        print(a)
#98