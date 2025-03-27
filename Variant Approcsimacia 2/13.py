from ipaddress import *

net = ip_network("172.16.80.0/255.255.248.0", 0)

c = 0
for ip in net:
    if f"{ip:b}".count("1") % 2 != 0:
        c += 1
        print(f"{ip:b}")
print(c)