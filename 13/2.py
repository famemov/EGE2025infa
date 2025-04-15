from ipaddress import ip_network

net = ip_network('5.2.5.0/255.255.0.0', 0)
k=0

#f'{ip:b}' можно юзать, не всегда работает
for ip in net:
    ip_bin=bin(int(ip))[2:].zfill(32) #обычный перевод, не легкий
    if ip_bin.count('0')%25==0:
        k+=1
print(k)

"""сколько в этой сети ip адрессов, для которых колво нулей
в двоичной записи кратно 25?"""