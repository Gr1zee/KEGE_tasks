from ipaddress import  *

address1 = ip_address("200.154.190.12")
address2 = ip_address("200.154.184.0")

for i in range(1, 33):
    net1 = ip_network(f"200.154.190.12/{i}", strict=False)
    net2 = ip_network(f"200.154.184.0/{i}", strict=False)
    if address1 in net2 and address2 in net1:
        # print(i, net1, net2)
        ...

for ip in ip_network("200.154.184.0/21"):
    print(ip)