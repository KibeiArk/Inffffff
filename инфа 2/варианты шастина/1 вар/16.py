def f(x):
    if x>400:
        return x**x
    if x<=400:
        return x + 6 +f(x+12)
print(f(72)-f(108))
#270