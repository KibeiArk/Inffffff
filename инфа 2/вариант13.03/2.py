print('w y x z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (w<=((x<=z)<=y))==0:
                    print(w,y,x,z)
#1=w 2=y 3=x 4=z