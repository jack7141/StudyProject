"""
리스코프 치환 원칙
설계시 안정성을 유지하기 위해 객체 타입이 유지해야하는 일련의 특성

객체의 안정성을 위해서 기존에 들어가는 데이터
>>> {'before': {'session': 0}, 'after': {'session': 1}}
위의 데이터와 마찬가지로 dict형식인지 확인하는 절차를 추가하려고 한다.
그리고 넘겨주는 데이터는 before, after가 값을 가지고 있어야하는 전제조건도 체크한다.

이렇게 하면 더욱 발전된 캡슐화를 가질 수 있다.

"""
from collections.abc import Mapping

class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meet_condition(event_data: dict):
        return False

    @staticmethod
    def validate_precondition(event_data: dict):
        """인터페이스 사전 조건 유효성 체크
        event_data가 우리가 원하는 데이터 형식인지 체크
        """
        if not isinstance(event_data, Mapping):
            raise ValueError(f"{event_data!r} dict가 아닙니다")
        for moment in ("before", "after"):
            if moment not in event_data:
                raise ValueError(f"{moment}는 {event_data}에서 누락되었습니다.")
            if not isinstance(event_data[moment], Mapping):
                # >>> ValueError: event_data['after'] dict가 아닙니다
                raise ValueError(f"event_data[{moment!r}] dict가 아닙니다")


class UnknownEvent(Event):
    """데이터만으로 식별할 수 없는 이벤트"""


class LoginEvent(Event):
    """로그인 사용자에 의한 이벤트"""

    @staticmethod
    def meet_condition(event_data: dict):
        return (
                event_data['before'].get('session') == 0
                and event_data['after'].get('session') == 1
        )


class LogoutEvent(Event):
    """로그아웃 사용자에 의한 이벤트"""

    @staticmethod
    def meet_condition(event_data: dict):
        return (
                event_data['before'].get('session') == 1
                and event_data['after'].get('session') == 0
        )


class TransactionEvent(Event):
    """시스템에서 발생한 트랜잭션 이벤트"""

    def __init__(self, event_data: dict):
        self.event_data = event_data

    @staticmethod
    def meet_condition(event_data: dict):
        # return True/False
        return event_data['after'].get('transaction') is not None


class SystemMonitor:
    """시스템에서 발생하는 이벤트 분기"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        # 올바른 이벤트 유형을 탐지하기 전에 사전조건을 먼저 검사한다.
        # 조건은 오직 'before', 'after'가 필수이고 그 값 또한 dict의 형식이여한다!!
        Event.validate_precondition(self.event_data)
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meet_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)


if __name__ == '__main__':
    """ 그래서 여기서 클래스 이름을 잡은 다음에 뭐 다시 어떻게 처리하려고? 여기서 분기를 태우는건 좀 이상한데?
    >>> LoginEvent
    >>> LogoutEvent
    >>> UnknownEvent
    >>> TransactionEvent
    """
    l1 = SystemMonitor({'before': {'session': 0}, 'after': {'session': 1}})
    print(l1.identify_event().__class__.__name__)
    l2 = SystemMonitor({'before': {'session': 1}, 'after': {'session': 0}})
    print(l2.identify_event().__class__.__name__)
    l3 = SystemMonitor({'before': {'session': 1}, 'after': ''})
    print(l3.identify_event().__class__.__name__)
    l4 = SystemMonitor({'after': {'transaction': 'Tx001'}})
    print(l4.identify_event().__class__.__name__)
