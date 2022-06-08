import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time




"""
* Multithreading
- Lock, DeadLock, Race Condition, Thread synchronization

세마포어 : 프로세스간 공유 된 자원에 접근시 문제 발생 가능성 -> 한개의 프로세스만 접근 처리(경쟁상태예방)
뮤텍스 : 공유된 자원의 데이터를 여러 스레드가 접근하는것을 막는것.(경쟁상태예방)
Lock : 상호 배제를 위한 잠금(lock) -> 데이터 경쟁
데드락(DeadLock) : 교착상태
뮤텍스와 세마포어의 차이는?
- 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
- 뮤택스 개체는 단일 스레드가 리소스 또는 중요 색션을 허용
- 세마포어는 리소스에 대한 제한 된 수의 동시 엑세스 허용
- 공간 갯수의 차이

"""

class FakeDataStore:
    # 공유변수(value)
    def __init__(self):
        # 현재 이 값은 데이터 영역과 Heap영역에서 공유가 된다
        # 현재 공유된 자원은 1개! -> self.value
        self.value = 0

    # 변수 없데이트 함수
    def update(self, n):
        logging.info(f"Thread update 시작 - {n}")

        # 뮤텍스, Lock 등 동기화(Thread synchroniziation)
        # self.value가 문제
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info(f"Thread update 끝 - {n}")

if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    store = FakeDataStore()

    logging.info(f"Test Start - {store.value}")

    with ThreadPoolExecutor(max_workers=2) as excutor:
        for n in ["First", "Second", "Third"]:
            excutor.submit(store.update, n)

    logging.info(f"Test END - {store.value}")

