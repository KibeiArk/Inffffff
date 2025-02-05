'''ТРЕУГ(A, 5, x) → ((МАКС(x, 11) ⩽ 19) ≡ ¬ТРЕУГ(23, 13, x))'''
def ter(x,a,y): return x+a>y and x+y>a and a+y > x
def f(x,a):return (ter(a,5,x)) <=(((max(x,11)) <=19) == (not(ter(23,13,x))))
for a in range(1,100):
    if all(f(x,a) for x in range(1,1000)):
        print(a)
#31