import concurrent.futures
import logging
import threading
import random
import queue
from concurrent.futures import ThreadPoolExecutor
import time

"""
* Multithreading
- 생산자 소비자 패턴(Producer/Consumer Pattern)

Producer-Consumer Pattern
1. 멀티스레드 디자인 패턴의 정석
2. 서버측 프로그래밍의 핵심
3. 주로 허리역할

Python Event 객체
1. Flag 초기값 0
2. set() -> 1, Clear() -> 0, Wait(1->리턴, 0->대기), isSet() -> 현 플래그 상태

"""

def producer(queue, event):
    """
    생산자
    네트워크 대기 상태라 가정(서버) IO작업
    """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f"생산자 - {message}")
        queue.put(message)
    logging.info(f"생산자 끝")

def consumer(queue, event):
    """
    소비자 CPU 작업
    응답 받고 소비하는 것으로 가정 or DB 저장
    """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f"소비자 저장 - {message}, size - {queue.qsize()}")


if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # A -> pipline -> B의 형식으로 처리하기 위함
    pipline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # 2개의 스레드를 만들고 각각의 스레드는 pipline을 통해서 통신한다.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline, event)
        executor.submit(consumer, pipline, event)

        # 실행시간 조정
        # while True:
        time.sleep(5)
        logging.info("Main: about to set event")
        event.set()


