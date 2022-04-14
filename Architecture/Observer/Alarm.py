import threading
import time

from datetime import datetime

class Alarm(threading.Thread):
    """
    * 주기적으로 알람이 발생할 때마다 구독자에게 알려주는 클래스
    """
    def __init__(self, duration=1):
        self.duration = duration
        # 구독자
        self.subsribers = []
        self.flag = True
        threading.Thread.__init__(self, None, None)

    def register(self, subscriber):
        """
        * 알림을 줄 구독자를 생성한다
        """
        self.subsribers.append(subscriber)

    def notify(self):
        """
        * 모든 구독자에게 알림을 준다
        """
        for subcriber in self.subsribers:
            subcriber.update(self.duration)

    def stop(self):
        """
        * Thread를 멈춘다
        """
        self.flag = False
    
    def run(self):
        """
        * 동작 시작
        """
        while self.flag:
            time.sleep(self.duration)
            # 알림
            self.notify()
