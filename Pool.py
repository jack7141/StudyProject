from multiprocessing import Pool
import multiprocessing as mp
import time
import os


def func(num):
    time.sleep(1)
    return num

def test():
    p = Pool(1)
    ret = p.apply_async(func, (1,))
    return ret.get(timeout=5)

if __name__ == '__main__':

    print(test())
