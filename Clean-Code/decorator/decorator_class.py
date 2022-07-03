

class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username" : self.event.username,
            "password": "**민감한 정보 삭제**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime('%Y-%m-%d %H:%M'),
        }

"""
여기서는 로그인 이벤트에 직접 매핑할 클래스를 선언했다.
이 클래스는 password 필드를 숨기고, timestamp 필드를 포매팅하는 기능이 들어있다.

이 방법은 처음에는 잘 동작하지만, 시작이 지나면서 시스템을 확장할수록 다음과 같은 문제가 발생하게 된다.

1. 클래스가 너무 많아진다 - 이벤트 클래스와 직렬화 클래스가 1대 1로 매핑되어 있으므로 직렬화 클래스가 점점 많아지게 된다.

2. 이러한 방법은 유연하지 못하다 - 만약 password를 가진 다른 클래스에서도 이 필드를 숨기려면 함수로 분리한 다음 여러 클래스에서 
호출해야한다. 이는 코드를 충분히 재사용했다고 볼 수 없다.

3. 표준화 - serialize() 메서드는 모든 이벤트 클래스에 있어야만 한다. 비록 믹스인을 사용해 다른 클래스로 분리할 수 있지만 상속을 제대로 사용
했다고 볼 수 없다.




class LoginEvent:
    
    SERIALIZER = LoginEventSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()


if __name__ == '__main__':
    loginevent = LoginEvent('test', 'asdf', '127.0.0.1', datetime.today())
    result = loginevent.serialize()
    print(result)
"""


"""좋은 예시"""
from datetime import datetime

def hide_field(field)->str:
    return "**민감한 정보 삭제**"

def format_time(field_timestamp: datetime)->str:
    return field_timestamp.strftime('%Y-%m-%d %H:%M')

def show_original(event_field):
    return event_field

class EventSerializer:
    def __init__(self, serialization_fields: dict)->None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in
            self.serialization_fields.items()
        }

class Serialization:
    def __init__(self, **transformation):
        self.serialization = EventSerializer(transformation)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class

@Serialization(
    username=show_original,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
class LoginEvent:

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def __repr__(self):
        return f"username: {self.username}, password: {self.password}, ip:{self.ip}, timestamp: {self.timestamp}"


if __name__ == '__main__':
    loginevent = LoginEvent('test', 'asdf', '127.0.0.1', datetime.today())
    print(loginevent)

