from ipaddress import *

c=0
for mask in range(0, 33):
    net = ip_network(f"221.142.14.0/{mask}", strict=False)
    ad = ip_address("221.142.0.0")
    if ad in net:
        c += 1
        print(net)
print(c)