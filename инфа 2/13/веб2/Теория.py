from ipaddress import*
'''
ip = ip_address('192.168.0.3')
print(f'{ip:b}') # двоичная запиьс айпи адреса'''
#net1 = ip_network('192.168.0.0/255.255.255.240')
#net = ip_network('192.168.0.0/28')
#Перебор айпи адресов в сети
#for ip in net:
  #  print(ip)
#Функция исправляет ишибку в записи адреса автоматически
net = ip_network('192.168.0.24/11',0)
print(net)
