print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a or b)<=((not(c))and a)) and d:
                    print(a,b,c,d)
#1=d 2=b 3=c 4=a
#dbca