"""
* Interface Segregation Principle, ISP 작은 인터페이스에 대한 가이드라인 제공

인터페이스란?
- 객체가 노출하는 메서드들의 집합, 즉 객체가 수신하거나 해석할 수 있는 모든 메세지가 인터페이스를 구성하며, 이것들은 다른 클라이언트에서 호출
할 수 있는 요청들이다. 인터페이스는 클래스에 노출된 동작의 정의와 구현을 분리한다.

인터페이스는 하나의 일만 담당해야한다라는 원칙이 더 맥락상 맞다.
"""

from abc import *

# EventParser라는 인터페이스 객체 내부 메소드들은 2가지 업무를 처리하고 있다.
# json 파싱과, xml파싱을 하고 있는데 이는 단일화 원칙에 어긋나기에 2개의 인터페이스로 나눠줘야함
class EventParser(metaclass=ABCMeta):
    """InterFace"""

    @abstractmethod
    def from_json(self, event_data):
        pass

    @abstractmethod
    def from_xml(self, event_data):
        pass


class JsonEventParser(metaclass=ABCMeta):
    """interface: Json event parser class"""
    @abstractmethod
    def from_json(self, event_data):
        pass



class XmlEventParser(metaclass=ABCMeta):
    """interface: xml event parser class"""
    @abstractmethod
    def from_xml(self, event_data):
        pass