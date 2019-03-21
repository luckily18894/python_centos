import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 关闭不必要的报错
from basic.ping_one import ping1
from paramiko_ssh import py_ssh


def ping_ssh(ipadd, usern, passw, cmd='ls'):
    for a in ipadd:
        if ping1(a) == '1':
            res = py_ssh(a, username=usern, password=passw, cmd=cmd)
            print('登陆'+a+'并'+cmd+'回显结果为：')
            print(res)
        else:
            print(a+'不通')


if __name__ == '__main__':
    l1 = ['192.168.1.104', '192.168.1.106']
    username = 'root'
    password = 'luCKi1y18894'
    ping_ssh(l1, username, password)



