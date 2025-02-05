from ipaddress import*
k=0
for mask in range(33):
    net = ip_network(f'76.155.48.2/{mask}',0)
    if str(net)== f'76.155.48.0/{mask}':
        k+=1
        print(net)
print(k)