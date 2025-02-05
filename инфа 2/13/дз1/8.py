'''Два узла, находящиеся в одной сети, имеют 
IP-адреса 121.171.5.70 и
121.171.5.107. Укажите наименьшее возможное количество 
адресов в этой сети.
'''
from ipaddress import*
for mask in range(33):
    net1 = ip_network(f'121.171.5.70/{mask}',0)
    net2 = ip_network(f'121.171.5.107/{mask}',0)
    if net1 ==net2:
        print(net1,net1.netmask, 2**(32-mask))
#64
