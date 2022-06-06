import logging
import threading
import time




"""
* Deamon Thread와 Join에 대해서

Deamon Thread 
- Background에서 실행
- 메인 스레드 종료시 즉시 종료됨(자신을 생성한 스레드가 종료되면 즉시 종료된다.)
- 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> 예시 기능) 노션에서 자동저장, 웹서버 

"""


# 스레드 함수 생성
def thread_function(name, d):
    """서브 스레드"""
    logging.info("서브 스레드 %s: 시작", name)
    for i in d:
        print(i)
    logging.info("서브 스레드 %s: 끝", name)



if __name__ == "__main__":
    # Loggin 포멧 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread 스레드 생성 전")

    # thread 생성 target: 실행할 스레드 함수, args: 스레드에 던져줄 인자
    # deamon: 부모의 업무가 끝나면 알아서 종료되버림, deamon과 join을 같이 쓰는건 의미 없다
    # 왜? 부모가 끝나면 자식이 끝나는걸 의도했는데, join을 사용하면 끝나지가 않으므로
    x = threading.Thread(target=thread_function, args=('one', range(200000)), daemon=True)
    y = threading.Thread(target=thread_function, args=('two', range(100000)), daemon=True)

    logging.info("Main-Thread 스레드 시작 전")

    x.start()
    y.start()

    # deamon Thread 확인
    # True/False
    print(x.isDaemon())

    # x.join()
    # y.join()

    logging.info("Main-Thread 스레드가 끝날때까지 대기")

    logging.info("Main-Thread 끝!")
