from ipaddress import ip_network

for m in range(0,33):
    net = ip_network(f'111.81.176.27/{m}',0)
    if str(net.network_address) == '111.81.160.0':
        print(net.netmask)