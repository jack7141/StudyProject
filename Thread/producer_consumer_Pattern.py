"""
멀티스레드 멀티프로세스 디자인 패턴의 정석
생산자 소비자 패턴(Producer/Consumer Pattern)

서버측 프로그래밍의 핵심
주로 허리역할

Python Event 객체 사용
1. Flag 초기값(0)
2. Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래스 상태 반환
"""

import concurrent.futures
import logging
import queue
import threading
import time
import random

def producer(queue, event):
    """생산자(네트워크 대기 상태라 가정(서버)"""
    # event는 초기값 0 -> is_set -> 1 즉, 1이 아니면!
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f"producer send message: {message}")
        queue.put(message)

    logging.info(f"producer event exit")


def consumer(queue, event):
    """소비자(증답 받고 소비하는 것으로 가정"""
    while not event.is_set() or not queue.empty():
        message = queue.get(message)
        logging.info(f"consumer storing message: {message}, {queue.qsize()}")
    logging.info(f"consumer recevied event exit")

if __name__ == "__main__":
    """
    Python Event 객체 사용
    1. Flag 초기값(0)
    2. Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래스 상태 반환
    """
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline, event)
        executor.submit(consumer, pipline, event)

    time.sleep(1)

    logging.info('set Event')

    # 프로그램 종료
    event.set()

