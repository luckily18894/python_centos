
import ipaddress
from basic.ping_one import ping1
from multiprocessing import Pool as ProcessPool


def multi_ping(ipadd):
    l1 = []
    db = {}
    pool = ProcessPool(processes=150)

    ipaddr = ipaddress.ip_network(ipadd)
    for ip in ipaddr:
        res = pool.apply_async(ping1, args=(str(ip),))
        db[str(ip)] = res

    pool.close()
    pool.join()

    for ipad, res in db.items():
        if db[ipad].get() == '1':
            l1.append(ipad)

    return l1


if __name__ == '__main__':
    import datetime
    import pickle

    time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    name = 'scan_save_pickle_' + time + '.pl'

    file = open(name, 'wb')
    pickle.dump(multi_ping('192.168.1.96/28'), file)
    file.close()

    file = open(name, 'rb')
    print(pickle.load(file))
