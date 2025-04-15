from ipaddress import ip_network

for m in range(0,33):
    net1=ip_network(f'216.54.187.235/{m}',0)
    net2=ip_network(f'216.54.174.128/{m}',0)
    if str(net1.network_address)!=str(net2.network_address):
        if '216.54.187.235'!= str(net1.network_address)and '216.54.174.128'!= str(net2.network_address):
            print(m)