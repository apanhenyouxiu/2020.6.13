import os
import time
from multiprocessing import Pool





def fun(i):
    print('子进程开始,pid = ' + str(os.getpid()) + '-' * 8 + str(i) + '-' * 8 + 'ppid = ' + str(os.getppid()))
    print('#' * 50)
    time.sleep(3)
    print('子进程结束,pid = ' + str(os.getpid()) + '-' * 8 + str(i) + '-' * 8 + 'ppid = ' + str(os.getppid()))
    print('#' * 50)


if __name__ == "__main__":
    #s = time.time()
    print('主进程pid：' + str(os.getpid()))
    #设置可供申请的进程最大数
    pool = Pool(processes=4)
    for i in range(7):
        #异步执行，非阻塞方式（添加进程后，立即执行）
        #pool.apply_async(fun,[i,])
        #阻塞方式执行（当一个进程执行完后再添加新的进程
        pool.apply(fun,[i,])
    #关闭进程池，关闭之后，将不能再向进程池添加新的进程
    pool.close()
    #当进程池中的所有进程都完成后，主进程才能执行
    pool.join()
    #print('耗时：{}s'.format(time.time() - s))
