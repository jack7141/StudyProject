"""
올바른 수준의 추상화 단계에서 예외 처리

- Error Handling - Execption
"""
import logging
import time

logger = logging.getLogger(__name__)

class Connector:
    """

    """
    def connect(self):
        return self

    @staticmethod
    def send(data):
        return data


class Event:
    def __init__(self, payload):
        self._payload = payload

    def decode(self):
        return f"decode {self._payload}"

def connect_with_retry(connector, retry_n_times, retry_threshold=5):
    """connector의 연결을 맺는다. <retry_n_times>회 재시도

    연결에 성공하면 connection 객체 변환
    재시도까지 모두 실패하면 ConnectionError 발생

    :param connector:           `.connect()` method를 가진 객체
    :param retry_n_times int:   ``connector.connect()``를 호출 시도하는 횟수
    :param retry_threshold int: 재시도 사이의 간격
    """
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(
                "%s: 새로운 연결 시도 %is", e, retry_threshold
            )
            time.sleep(retry_threshold)
    exc = ConnectionError(f"{retry_n_times} 번째 재시도 연결 실패")
    logger.exception(exc)
    raise exc

class DataTransport:
    """추상화 수준에 따른 예외 분리를 한 객체의 예제"""

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.connection = connect_with_retry(
            self._connector, self.retry_n_times, self.retry_threshold
        )
        self.send(event)

    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error("%r 잘못된 데이터 포함: %s", event, e)
            raise

if __name__ == "__main__":
    connectorObj = Connector()
    eventObj = Event("Hello World")
    dataobj = DataTransport(connectorObj)
    dataobj.deliver_event(eventObj)


