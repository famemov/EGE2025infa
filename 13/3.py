from ipaddress import ip_network

net = ip_network('112.160.0.0/255.240.0.0')

k=0

for ip in net:
    ip_bin=bin(int(ip))[2:].zfill(32)
    if ip_bin.count('1')%5==0:
        k+=1
print(k)