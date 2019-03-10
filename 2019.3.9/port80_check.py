
import os
import re
import time


while True:
    result = os.popen("netstat -tulnp").read()
    l1 = result.split('\n')

    for a in l1:
        if re.match('\s*tcp\s*.*\d:80', a):
            print('HTTP(TCP/80)服务已经被打开')
            break
    else:
        print('等待一秒重新开始监控')
        time.sleep(1)
        continue
    break

