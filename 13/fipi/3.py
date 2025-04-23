from ipaddress import ip_network

for m in range(0,33):
    net = ip_network(f'179.57.101.43/{m}',0)
    if str(net.network_address)=='179.57.64.0':
        print(net.netmask)