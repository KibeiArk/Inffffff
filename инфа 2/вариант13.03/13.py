from ipaddress import*
for mask in range(33):
    net = ip_network(f'203.155.64.98/{mask}',0)
    print(net)
#25