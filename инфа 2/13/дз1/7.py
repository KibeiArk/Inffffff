'''Два узла, находящиеся в одной сети, имеют 
IP-адреса 112.117.107.70 и
112.117.121.80. Укажите наибольшее возможное значение 
третьего слева байта
маски сети. Ответ запишите в виде десятичного числа.'''
from ipaddress import*
ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(33):
    net1 = ip_network(f'112.117.107.70/{mask}',0)
    net2 = ip_network(f'112.117.121.80/{mask}',0)
    if net1 == net2 and net1[0] < ip1 < net1[-1] and net2[0] < ip2 < net2[-1]:
        print(net1,net1.netmask)
#224