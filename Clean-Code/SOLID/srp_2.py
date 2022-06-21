"""
개방/폐쇄 원칙
클래스를 디자인 할때는 유지보수가 쉽도록 로직을 캡슐화하여 확장에는 개방적이고, 수정에는 폐쇄적으로 해야한다.
쉬운말로 확장이 용이하고, 새로운 기능은 기존의 코드를 수정하는 것이 아닌 추가하는 방식으로 진행 되어야한다.

1번의 방식보다 훨씬 좋아졌지만, 문제점이 있다.
1. 이벤트 유형을 결정하는 논리가 일체형으로 중앙 집중화된다(SystemMonitor)
지원하려는 이벤트가 늘어날수록 메서드도 커질 것이므로 결국 큰 메스드가 될 수 있다

2. 새로운 유형의 메소드가 들어올때마다 elif를 남발하게 된다. 가독성에서 최악이다!!
"""
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

class UnknownEvent(Event):
    """데이터만으로 식별할 수 없는 이벤트"""

class LoginEvent(Event):
    """로그인 사용자에 의한 이벤트"""

class LogoutEvent(Event):
    """로그아웃 사용자에 의한 이벤트"""

class SystemMonitor:
    """시스템에서 발생하는 이벤트 분기"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if(
            self.event_data['before']['session'] == 0
            and self.event_data['after']['session'] == 1
        ):
            return LoginEvent(self.event_data)
        elif (
            self.event_data['before']['session'] == 1
            and self.event_data['after']['session'] == 0
        ):
            return LogoutEvent(self.event_data)

        return UnknownEvent(self.event_data)


if __name__ == '__main__':
    l1 = SystemMonitor({'before': {'session': 0}, 'after': {'session': 1}})
    print(l1.identify_event().__class__.__name__)
    l2 = SystemMonitor({'before': {'session': 1}, 'after': {'session': 0}})
    print(l2.identify_event().__class__.__name__)
    l3 = SystemMonitor({'before': {'session': 1}, 'after': {'session': 1}})
    print(l3.identify_event().__class__.__name__)