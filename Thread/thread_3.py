import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time




"""
* TreadPoolExecutor
- 많은 스레드 생성, concurrent, futures, (xxx)PoolExecutor

그룹 스레드
python 3.2 이상 표준 라이브러리 사용
concurrnet, futures
with 사용으로 생성, 소멸 라이프사이클 관리 용이
디버깅하기가 난해함
대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)
"""


# 스레드 함수 생성
def task(name):
    logging.info("서브 스레드 %s: 시작", name)

    result = 0
    for i in range(10):
        result += i

    logging.info('서브 스레드 %s: 끝 result: %d', name, result)

    return result

def main():
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread 스레드 생성 전")

    logging.info("Main-Thread 스레드 시작 전")

    # 실행방법 1
    # max_worker : 작업의 개수가 넘어가면 직접 설정이 유라
    # 아래의 방식은 clean code는 아니므로 with문을 사용해서 처리한다
    """
    excutor = ThreadPoolExecutor(max_workers=3)
    task1 = excutor.submit(task, ('first',))
    task2 = excutor.submit(task, ('two',))
    task3 = excutor.submit(task, ('three',))

    print(task1.result())
    print(task2.result())
    print(task3.result())
    14:01:58 : Main-Thread 스레드 생성 전
    14:01:58 : Main-Thread 스레드 시작 전
    14:01:58 : 서브 스레드 ('first',): 시작
    14:01:58 : 서브 스레드 ('first',): 끝 result: 49995000
    14:01:58 : 서브 스레드 ('two',): 시작
    14:01:58 : 서브 스레드 ('two',): 끝 result: 49995000
    14:01:58 : 서브 스레드 ('three',): 시작
    14:01:58 : 서브 스레드 ('three',): 끝 result: 49995000
    49995000
    49995000
    49995000
    """

    # 실행방법 2
    # with를 사용하여 라이프사이클 관리
    with ThreadPoolExecutor(max_workers=10) as excutor:
        tasks = excutor.map(task, ['first', 'Second'])
        print(list(tasks))


if __name__ == "__main__":
    main()
