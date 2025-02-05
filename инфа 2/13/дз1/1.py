'''Для узла с IP-адресом 220.128.112.142 адрес сети
равен 220.128.96.0. Чему равен
третий слева байт маски? Ответ запишите в 
виде десятичного числа.
'''
from ipaddress import*
for mask in range(33):
    net = ip_network(f'220.128.112.142/{mask}',0)
    if str(net) == f'220.128.96.0/{mask}':
        print(net,net.netmask)
#224