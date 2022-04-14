from datetime import datetime
from time import sleep
from time import *            
import time

from Architecture.Observer.Alarm import Alarm


class DumbClock(object):
    """
    *구독자는 알람을 위해 간단한 DumbClock 클래스로 Alarm 객체를 구독하고, 이를 사용해 시간을 업데이트한다.
    """
    def __init__(self):
        # 시작시간
        self.current = time.time()


    def update(self, *args):
        """
        * 구독자로부터 콜백!
        """
        self.current += args[0]
    
    def __str__(self):
        """
        시간 표시
        """
        return datetime.fromtimestamp(self.current).strftime('%H:%M:%S')


if __name__ == '__main__':
    # 먼저 1초를 주기로 갖는 알람을 생성해보자
    alarm = Alarm(duration=1)
    
    clock = DumbClock()
    
    # 옵저버로 clock 객체를 alarm 객체에 등록해 통보를 수신할 수 있다.
    alarm.register(clock)

    print(clock)
    time.sleep(20)
    print(clock)

