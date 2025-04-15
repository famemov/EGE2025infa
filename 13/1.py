def f():
    print('------------------------')

from ipaddress import ip_network

net = ip_network('218.194.82.148/255.255.255.192', 0) #узел + маска

print(net.netmask) # выводим маску сети

f()

print(net.network_address) # выводим адрес сети

f()

for ip1 in net: # все адреса сети
    print(ip1)

f()

for ip2 in net.hosts(): # все адреса сети без нулегого и щирика (импостеров)
    print(ip2)