'''Сеть задана IP-адресом одного из входящих в неё узлов 158.214.121.40 и сетевой маской 255.255.255.224.

Найдите наименьший IP-адрес в данной сети, который может быть назначен компьютеру.

В ответе укажите найденный IP-адрес без разделителей.'''
from ipaddress import*
ant = []
net = ip_network('158.214.121.40/255.255.255.224',0)
for ip in net:
    print(ip)
#15821412133