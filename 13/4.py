from ipaddress import ip_network
#задания на нахождение самой маски

for m in range(0,33):
    net=ip_network(f'218.48.192.56/{m}', 0) # юзаем узел сети
    if str(net.network_address) == '218.48.192.0': # проверка что это тот самый адресс сети
        if len(list(net.hosts())) >= 500: # что в сети не менее 500 узлов
            print(net.netmask)