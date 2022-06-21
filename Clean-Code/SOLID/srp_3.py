"""
개방/폐쇄 원칙
클래스를 디자인 할때는 유지보수가 쉽도록 로직을 캡슐화하여 확장에는 개방적이고, 수정에는 폐쇄적으로 해야한다.
쉬운말로 확장이 용이하고, 새로운 기능은 기존의 코드를 수정하는 것이 아닌 추가하는 방식으로 진행 되어야한다.

TIP:
__subclassess__() 매직메소드를 활용해 이벤트 유형을 찾는다.
이렇게 하면 새로운 유형의 이벤트를 지원하려면 단지 Event 클래스를 상속 받아 비즈니스 로직에 따라 meet_condition()메소드를 구현하기만 하면
된다.
"""
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meet_condition(event_data: dict):
        return False

class UnknownEvent(Event):
    """데이터만으로 식별할 수 없는 이벤트"""

class LoginEvent(Event):
    """로그인 사용자에 의한 이벤트"""
    @staticmethod
    def meet_condition(event_data: dict):
        return (
            event_data['before']['session'] == 0
            and event_data['after']['session'] == 1
        )

class LogoutEvent(Event):
    """로그아웃 사용자에 의한 이벤트"""
    @staticmethod
    def meet_condition(event_data: dict):
        return (
            event_data['before']['session'] == 1
            and event_data['after']['session'] == 0
        )

class SystemMonitor:
    """시스템에서 발생하는 이벤트 분기"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meet_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)


if __name__ == '__main__':
    l1 = SystemMonitor({'before': {'session': 0}, 'after': {'session': 1}})
    print(l1.identify_event().__class__.__name__)
    l2 = SystemMonitor({'before': {'session': 1}, 'after': {'session': 0}})
    print(l2.identify_event().__class__.__name__)
    l3 = SystemMonitor({'before': {'session': 1}, 'after': {'session': 1}})
    print(l3.identify_event().__class__.__name__)