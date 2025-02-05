'''Для узла с IP-адресом 108.133.75.91 адрес сети равен 108.133.75.64. Чему равно
наибольшее количество возможных адресов в этой сети?'''
from ipaddress import*
for mask in range(33):
    net = ip_network(f'108.133.75.91/{mask}',0)
    if str(net)== f'108.133.75.64/{mask}':
        print(net,net.netmask,2**(32-mask))
#64