from fnmatch import*
k =0
ans =[]
for i in range(1,10**9,3057):
    if fnmatch(str(i),'1?58*5?9'):
        print(i,i//3057)