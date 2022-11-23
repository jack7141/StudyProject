import logging
import os
import random
import time
from multiprocessing import Process, current_process

def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name
    result = n * n
    print(f"Process ID: {process_id}, Process Name: {process_name}")
    print(f"Result of {n} square: {result}")

if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f"parent process ID {parent_process_id}")

    processes = list()

    for i in range(1, 500):
        t = Process(name=str(i), target=square, args=(i,))

        processes.append(t)

        # 시작
        t.start()

    for p in processes:
        p.join()