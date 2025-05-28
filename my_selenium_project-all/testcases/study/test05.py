import os
import timeit

import psutil
from functools import wraps
import time




def perf_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f'{func.__name__} took {elapsed_time:.6f} seconds')
    return wrapper


# 显示当前python占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()  # 返回一个命令tuple
    memory = info.uss / 1024 / 1024
    print(f'{hint} memory used: {memory} MB')


def test_iterator():
    show_memory_info('initing iterator')
    lst_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(lst_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    lst_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(lst_2))
    show_memory_info('after sum called')

if __name__ == '__main__':

    # test_iterator_exec_time = timeit.timeit(test_iterator, number=1)
    test_iterator_exec_time = timeit.repeat(test_iterator, number=1, repeat=3)
    print(f'平均iterator execution time: {sum(test_iterator_exec_time)/len(test_iterator_exec_time):.6f} seconds')

    # test_generator_exec_time = timeit.timeit(test_generator, number=1)
    test_generator_exec_time = timeit.repeat(test_generator, number=1, repeat=3)
    print(f'平均generator execution time: {sum(test_generator_exec_time)/len(test_generator_exec_time):.6f} seconds')