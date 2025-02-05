'''Для узла с IP-адресом 241.185.253.57 адрес сети равен 241.185.252.0. Найдите
наименьшее возможное количество нулей в двоичной записи маски подсети.'''
from ipaddress import*
for mask in range(33):
    net = ip_network(f'241.185.253.57/{mask}',0)
    if str(net) == f'241.185.252.0/{mask}':
        print(net,net.netmask,(32-mask))
#9