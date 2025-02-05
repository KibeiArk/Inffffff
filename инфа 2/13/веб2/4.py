from ipaddress import*
k=0
for mask in range(33):
    net = ip_network(f'151.168.147.193/{mask}',0)
    if str(net)== f'151.168.147.128/{mask}':
        k+=1
        print(net)
print(k)
#25