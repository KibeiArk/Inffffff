print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x==(y<=(z or x))) and w):
                    print(x, y, z,w)
'''
x y z w
0 1 0 1
1 0 0 1
1 0 1 1
1 1 0 1'''
# 1 =x 2=y 3=w 4=z
#xywz