from ipaddress import ip_network
#дано было вот это 116.242.{A}.26/255.255.255.224 и найти макс А если условия
for A in range(0,256):
    net=ip_network(f'116.242.{A}.26/255.255.255.224', 0)
    uslovia = [bin(int(ip))[2:].zfill(32)[:16].count('1') >= bin(int(ip))[2:].zfill(32)[16:].count('1') for ip in net]
    if all(uslovia):
        print(A)