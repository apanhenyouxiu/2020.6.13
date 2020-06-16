import os
import time
from multiprocessing import Process



'''直接使用Process类'''

def fun(i):
    print('子进程开始,pid = ' + str(os.getpid()) + '-' * 8 + str(i) + '-' * 8 + 'ppid = ' + str(os.getppid()))
    print('#' * 50)
    time.sleep(5)
    print('子进程结束,pid = ' + str(os.getpid()) + '-' * 8 + str(i) + '-' * 8 + 'ppid = ' + str(os.getppid()))
    print('#' * 50)


if __name__ == "__main__":
    #s = time.time()
    print('主进程pid：' + str(os.getpid()))
    for i in range(3):
        p = Process(target=fun,args=[i,])
        p.start()
    
    #print('耗时：{}s'.format(time.time() - s))
