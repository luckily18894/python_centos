
import ipaddress
from ping_one import ping1
from multiprocessing import Pool as ProcessPool
from multiprocessing import freeze_support


def multi_ping(ipadd):
    pool = ProcessPool(processes=150)

    l1 = []
    ipaddr = ipaddress.ip_network(ipadd)
    for ip in ipaddr:
        if pool.apply_async(ping1, args=(str(ip),)).get() == '1':
            l1.append(str(ip))

    pool.close()
    pool.join()

    return l1


if __name__ == '__main__':
    print(multi_ping('192.168.1.96/28'))

