from ipaddress import ip_network

for m in range(0,33):
    net=ip_network(f'57.179.208.27/{m}',0)
    if str(net.network_address)=='57.179.192.0':
        print(f'{net.netmask:b}'.count('1'))
#Для узла с IP-адресом 57.179.208.27 адрес сети равен 57.179.192.0. Каково наибольшее возможное количество единиц в разрядах маски?