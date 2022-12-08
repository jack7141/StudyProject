# coding=utf-8
"""
Queue, Pipe, Communications between process
"""
import logging
from multiprocessing import Process, Queue, current_process, Pipe
import os
import time

def worker(id, base_num, connection: Pipe):
    process_name = current_process().name

    # 누적
    sub_total = 0

    for i in range(base_num):
        sub_total += 1

    # Produce
    connection.send(sub_total)
    connection.close()

    print(f"Process ID - {id}, Process Name - {process_name}")
    print(f"Result : {sub_total}")

def main():
    # 부모 프로세스 ID
    parents_process_id = os.getpid()
    logging.info(f"parents_process_id: {parents_process_id}")


    # 시작 시간
    start_time = time.time()

    # Queue 선언
    parent_pipe, child_pipe = Pipe()

    t = Process(name=str(parents_process_id), target=worker, args=(parents_process_id, 100000000, child_pipe))
    t.start()

    t.join()

    logging.info(f"---{time.time() - start_time} seconds---")


    print()
    print(f"Main-Processing Total Count - {parent_pipe.recv()}")
    print("FIN")


if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
