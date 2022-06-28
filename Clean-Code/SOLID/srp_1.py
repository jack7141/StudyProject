"""SRP를 준수하지 않은 디자인

* 하위의 클래스는 각각이 독립적으로 동작하는 메서드들을 하나의 인터페이스에 정의했다는 점이다.
각각의 동작은 독립적으로 운용될 수 있고, 이 예제에서는 각각의 메소드가 클래스의 행동을 대표하기 때문에, 하나가 망가지면,
다른 메소드도 같이 수정하는 불상사가 발생할 수 있다. 다음 예제에서 좀더 나은 방식으로 클래스를 분산하고, 각 클래스들마다 단일의 책임을
지도록 한다.
"""

class SystemMonitor:
    def load_activity(self):
        """소스에서 처리할 이벤트 가져오기"""

    def indentify_events(self):
        """가져온 데이터를 파싱하여 도메인 객체 이벤트로 변환"""

    def stream_events(self):
        """파싱한 이벤트를 외부 에이전트로 전송"""