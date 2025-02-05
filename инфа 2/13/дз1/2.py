'''Для узла с IP-адресом 115.12.69.38 адрес 
сети равен 115.12.64.0. Найдите
наименьшее возможное количество единиц в двоичной 
записи маски подсети.
'''
from ipaddress import*
for mask in range(33):
    net = ip_network(f'115.12.69.38/{mask}',0)
    if str(net)==f'115.12.64.0/{mask}':
        print(net,net.netmask)
#18