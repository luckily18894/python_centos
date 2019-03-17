
import ipaddress
from ping_one import ping1


def multi_ping(ipadd):
    l1 = []
    # ipaddr = ipaddress.ip_network('192.168.1.0/29')
    ipaddr = ipaddress.ip_network(ipadd)
    for ip in ipaddr:
        if ping1(str(ip)) == '1':
            l1.append(str(ip))
    return l1


if __name__ == '__main__':
    print(multi_ping('192.168.1.0/29'))




