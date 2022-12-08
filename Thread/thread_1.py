import logging
import threading
import time


# 스레드 함수 생성
def thread_function(name):
    """서브 스레드"""
    logging.info("서브 스레드 %s: 시작", name)
    time.sleep(5)
    logging.info("서브 스레드 %s: 끝", name)


if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread 스레드 생성 전")

    # thread 생성 target: 실행할 스레드 함수, args: 스레드에 던져줄 인자
    x = threading.Thread(target=thread_function, args=('start', ))

    logging.info("Main-Thread 스레드 시작 전")

    x.start()

    # x.join()

    logging.info("Main-Thread 스레드가 끝날때까지 대기")

    logging.info("Main-Thread 끝!")

    """
    12:32:27 : Main-Thread 스레드 생성 전
    12:32:27 : Main-Thread 스레드 시작 전
    12:32:27 : 서브 스레드 start: 시작
    12:32:27 : Main-Thread 스레드가 끝날때까지 대기
    12:32:27 : Main-Thread 끝! --> 메인은 끝났지만 서브스레드는 아직 진행중이기 때문에 하위 로그가 찍힌다.
    12:32:32 : 서브 스레드 start: 끝 --> 서브 스레드 완료!
    
    즉, 부모 프로그램은 끝나도 자식 프로그램(스레드)는 계속 동작한다.
    만약, 자식 스레드가 끝날때까지 부모 스레드를 대기 시키고 싶다면?
    >>> .join()을 사용해서 대기 시킬 수 있다.
    """

    """
    .join()을 사용시
    
    12:35:33 : Main-Thread 스레드 생성 전
    12:35:33 : Main-Thread 스레드 시작 전
    12:35:33 : 서브 스레드 start: 시작
    12:35:38 : 서브 스레드 start: 끝
    12:35:38 : Main-Thread 스레드가 끝날때까지 대기
    12:35:38 : Main-Thread 끝!
    
    """