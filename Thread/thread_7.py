# coding=utf-8
"""
Queue, Pipe, Communications between process
"""
import logging
from multiprocessing import Process, Queue, current_process
import os
import time

def worker(id, base_num, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    for i in range(base_num):
        sub_total += 1

    # Produce
    q.put(sub_total)

    print(f"Process ID - {process_id}, Process Name - {process_name}, ID: {id}")
    print(f"Result : {sub_total}")

def main():
    # 부모 프로세스 ID
    parents_process_id = os.getpid()
    logging.info(f"parents_process_id: {parents_process_id}")

    # 프로세스 리스트 선언
    processes = list()

    # 시작 시간
    start_time = time.time()

    # Queue 선언
    q = Queue()

    for i in range(20):
        t = Process(name=str(i), target=worker, args=(i, 100000000, q))
        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()

    for precess in processes:
        precess.join()

    logging.info(f"---{time.time() - start_time} seconds---")

    q.put("exit")

    total = 0

    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()
    print(f"Main-Processing Total Count - {total}")
    print("FIN")


if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
