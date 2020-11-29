import random
from multiprocessing.pool import Pool
from time import sleep, time

import os


def run(name):
    print("%s子进程开始，进程ID：%d" % (name, os.getpid()))
    start = time()
    # sleep(random.choice([1, 2, 3, 4]))
    sleep(2)
    end = time()
    print("%s子进程结束，进程ID：%d。耗时0.2 %f" % (name, os.getpid(), end-start))


if __name__ == "__main__":
    print("父进程开始")
    # 创建多个进程，表示可以同时执行的进程数量。默认大小是CPU的核心数
    p = Pool(6)
    for i in range(6):
        # 创建进程，放入进程池统一管理
        p.apply_async(run, args=(i,))
    # 如果我们用的是进程池，在调用join()之前必须要先close()，并且在close()之后不能再继续往进程池添加新的进程
    p.close()
    # 进程池对象调用join，会等待进程吃中所有的子进程结束完毕再去结束父进程
    p.join()
    print("父进程结束。")