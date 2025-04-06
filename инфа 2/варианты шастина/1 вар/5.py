for n in range(1,100):
    b = f'{n:b}'
    if b.count('1')%2==0:
        b +='11'
    else:
        b+='01'
    r = int(b,2)
    if r>61:
        print(r)
        break
#63