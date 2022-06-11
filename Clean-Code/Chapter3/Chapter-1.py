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


class DataTransport:
    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        # ConnectionError와 ValueError는 상호 관계가 없다.
        # 그렇기 때문에 매우 다른 유형의 에러 처리 유형을 분산해야한다.
        # 명시적으로 하기 위해 ConnectionError는 connect 함수에서 처리 되어야한다.
        # 반대로, ValueError는 event의 decode에 속한 에러이다.
        # 위의 생각을 코드로 수정하게 되면 현재 이 함수내에서는 에러를 catch할 필요가 없어진다.
        except ConnectionError as e:
            logger.info("connection error detected %s", e)
            raise
        except ValueError as e:
            logger.error("%r 데이터 형식이 올바르지 않습니다. %s", event, e)
            raise


    def connect(self):
        for _ in range(self.retry_n_times):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info("$s: 새로운 연결을 시도합니다. %is", e, self.retry_threshold,)
                time.sleep(self.retry_threshold)
            else:
                return self.connection
        raise ConnectionError(f"연결을 {self.retry_n_times} 차례 진행했지만 연결할 수 없습니다.")

    def send(self, data):
        return self.connection.send(data)

