'''(М. Ишимов) В терминологии сетей ТСР/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится 
к адресу сети, а
какая - к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и 
маске сети. Сеть, в которой содержится узел с IP-адресом 99.8.254.232, задана маской сети 255.255.А.0, где А - некоторое допустимое 
для записи маски число. Определите минимальнде значение А, для которого для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное 
количество единиц в левых двух байтах не более суммарного количества единиц в правых двух байтах.
В ответе укажите только число.'''
from ipaddress import*
for mask in range(16,25):
    net = ip_network(f'99.8.254.232/{mask}',0)
    if all(f'{ip:b}'[0:16].count('1')<=f'{ip:b}'[16:32].count('1') for ip in net ):
        print(net.netmask)
#248



