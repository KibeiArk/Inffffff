from ipaddress import*
k=0
net = ip_network('228.172.236.0/255.255.240.0',0)
for ip in net:
    b = f'{ip:b}'
    if b.count('1') %5!=0:
        k+=1
print(k)
#3381