# coding=utf-8
"""
Queue, Pipe, Communications between process
부모 스레드와 자식 스레드간의 1:1 통신을 하기 위해서 사용하고, 데이터가 흘리는게 없어야하는 상황에서 사용한다.
강의 multiprocess(5) - Queue, Pipe
"""
import logging
from multiprocessing import Process, Queue, current_process, Pipe
import os
import time

def worker(id, base_num, connection):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    for i in range(base_num):
        sub_total += 1

    # Pipe 생성
    connection.send(sub_total)
    connection.close()

    print(f"Process ID - {process_id}, Process Name - {process_name}, ID: {id}")
    print(f"Result : {sub_total}")

def main():
    # 부모 프로세스 ID
    parents_process_id = os.getpid()
    logging.info(f"parents_process_id: {parents_process_id}")


    # 시작 시간
    start_time = time.time()

    # Pipe 선언(부모와 자식을 생성할 수 있음- Pipe 객체 생성시)
    # 단일이기 때문에, 따로 리스트를 생성하거나 Queue를 생성할 필요가 없어진다.
    parant_conn, child_conn = Pipe()

    t = Process(name=str(parents_process_id), target=worker, args=(parents_process_id, 100000000, child_conn))

    # 시작
    t.start()

    t.join()

    logging.info(f"---{time.time() - start_time} seconds---")

    print()
    # child_conn 자식을 traget함수로 보내고 그 함수안에서 send로 던졌기 때문에 부모는 아래처럼 recv함수를 통해서 값을 얻을 수 있음
    print(f"Main-Processing Total Count - {parant_conn.recv()}")
    print("FIN")


if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
