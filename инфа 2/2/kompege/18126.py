print('w x y z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((z == x)<=w) and(w<=(y and x))):
                    print(w,x,y,z)
'''
w x y z
0 0 0 1
0 0 1 1
0 1 0 0
0 1 1 0
1 1 1 0'''
#1=x 2=z 3=y 4=w
#yzxw